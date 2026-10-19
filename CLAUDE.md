# BiharParichay-Project

Shared engineering standard: @.claude/engineering-standards.md. It applies to all work in this repository. This file adds what is specific to the project, and wins where the two disagree.

Bihar Parichay, a static resource on Bihar's society, economy, geography and
culture, live at bihar-parichayproject.netlify.app. No build step. `netlify.toml`
publishes the repository root, and `.github/workflows/static.yml` also
publishes it to GitHub Pages. `README.md` describes the sections.

## Commands

```bash
python3 scripts/check.py      # run by CI
python3 -m http.server 8000
```

There is no project history recorded here yet. When a decision or a trap is
found, write it down in this file.
