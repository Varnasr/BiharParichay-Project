#!/usr/bin/env python3
"""Static checks for the Bihar Parichay dashboard.

    python3 scripts/check.py

No network and no dependencies. The only workflow here deployed to Pages and
validated nothing, so none of the invariants below were checked by anything.

The site is one 718 KB `index.html` with everything inline. That shape makes
two ordinary things dangerous, and both are checked here.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
checks = 0

# Markers that a matched href/src is a JavaScript expression, not a path.
CONCAT = re.compile(r"""[\s'"+${}<>\\]""")


def check(name, ok, detail=''):
    global checks
    checks += 1
    if not ok:
        errors.append('%s: %s' % (name, detail))


def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8', errors='replace') as fh:
        return fh.read()


def main():
    index = read('index.html')
    sw = read('sw.js')

    check('index.html sets a viewport',
          re.search(r'<meta[^>]*name=["\']?viewport', index, re.I) is not None,
          'a phone lays the page out at desktop width and zooms out')
    check('index.html declares a language',
          re.search(r'<html[^>]*\blang=', index, re.I) is not None,
          'a screen reader guesses the pronunciation, and half this page is Devanagari')
    check('index.html has a title', re.search(r'<title>[^<]+</title>', index), 'empty or absent')

    # ---------------------------------------------------------- the two hazards
    # 1. Everything is inline and there is no Content-Security-Policy. The page
    # carries 83 inline event handlers and its whole application in a <script>
    # block, so adding `script-src 'self'` would take the dashboard down to a
    # static shell with nothing on the page to say why. If a policy is ever
    # wanted here, the handlers move into a file first.
    inline = len(re.findall(r'\son(?:click|change|input|submit|load|error|keyup|keydown|mouseover)\s*=', index))
    check('there are inline handlers to protect', inline > 0, 'none found, so this check is moot')
    toml = read('netlify.toml')
    has_csp = 'Content-Security-Policy' in toml or 'Content-Security-Policy' in index
    check('no Content-Security-Policy while %d inline handlers are in use' % inline,
          not has_csp,
          'a policy without unsafe-inline silently disables every one of them; '
          'move the handlers into a script file first')

    # 2. `cache.addAll` is all or nothing. This service worker precaches five
    # third-party origins, so the install depends on Google Fonts, cdnjs,
    # unpkg and jsDelivr all answering at that moment. One slow or missing
    # response rejects the whole promise, the install fails, and the site
    # silently ships with no offline layer. Nothing on the page says so.
    m = re.search(r'const ASSETS = \[(.*?)\];', sw, re.S)
    check('sw.js declares its precache list', m is not None, 'const ASSETS not found')
    if m:
        assets = re.findall(r"'([^']+)'", m.group(1))
        local = [a for a in assets if not a.startswith('http')]
        remote = [a for a in assets if a.startswith('http')]
        check('sw.js precaches something', assets, 'empty')
        gone = [a for a in local
                if not os.path.exists(os.path.join(ROOT, a.lstrip('/') or 'index.html'))]
        check('every local precached path is on disk', not gone,
              'would reject cache.addAll and fail the install: %s' % gone)
        # Not a failure, but it must not grow unnoticed: each origin added here
        # is one more third party that can fail the install.
        origins = sorted({re.match(r'https://[^/]+', a).group(0) for a in remote})
        check('the precache depends on no more than four third-party origins',
              len(origins) <= 4,
              '%d origins, each of which can fail the install on its own: %s'
              % (len(origins), origins))

    check('sw.js carries a cache name',
          re.search(r"CACHE_NAME\s*=\s*'([^']+)'", sw) is not None,
          'without one the cache is never rotated and returning visitors keep the old page')

    # index.html is precached, so a returning visitor keeps whichever copy they
    # hold until CACHE_NAME changes. There is no way to check from one commit
    # that it was bumped; this at least pins that the page is precached, so the
    # dependency stays visible.
    if m:
        check('index.html is precached, so CACHE_NAME must be bumped when it changes',
              any(a in ('/', '/index.html') for a in assets),
              'no longer precached, so this note needs revisiting')

    # ------------------------------------------------------------- references
    on_disk = set()
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != '.git']
        for f in filenames:
            rel = os.path.relpath(os.path.join(dirpath, f), ROOT).replace('\\', '/')
            on_disk.add('/' + rel)
    broken, refs = [], 0
    for mm in re.finditer(r'(?:href|src)="([^":#?]+)"', index):
        raw = mm.group(1)
        if raw.startswith(('http', 'mailto:', 'tel:', 'data:', '#')) or not raw:
            continue
        # The whole application is inline, so this scan walks JavaScript as
        # well as markup and picks up strings being concatenated into markup,
        # such as href="' + r.url + '". Those reference nothing on disk. Skip
        # any candidate carrying concatenation, interpolation or whitespace.
        if CONCAT.search(raw):
            continue
        refs += 1
        target = raw if raw.startswith('/') else '/' + raw
        if target not in on_disk:
            broken.append(raw)
    check('all %d local references resolve' % refs, not broken,
          '%d broken: %s' % (len(broken), broken[:6]))

    if errors:
        print('FAIL: %d of %d checks' % (len(errors), checks))
        for e in errors:
            print('  - %s' % e)
        return 1
    print('PASS: %d checks' % checks)
    return 0


if __name__ == '__main__':
    sys.exit(main())
