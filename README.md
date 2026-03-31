# Bihar Parichay
*Understanding Bihar -- Society, Economy, Geography, Culture, and the People*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Live**: [on-web.link/BiharParichay](https://on-web.link/BiharParichay)

## What is this?

Bihar Parichay is an interactive resource for understanding Bihar -- its people, problems, politics, and possibilities. It combines data, stories, maps, and research tools into a single site designed for anyone who needs to know what is actually happening in Bihar.

This is not a textbook or a tourism site. It is a working resource built for people who engage with Bihar professionally -- researchers, journalists, policy workers, political organisers, and fieldworkers conducting listening circles.

## What's inside

| Section | What it covers |
|---------|---------------|
| **Overview** | 128 million people, 51.9% poverty, the core paradox |
| **Geography** | North-South divide, flood politics, Nepal water nexus, Diara lands |
| **Society** | Caste structure, land ownership, electoral sociology, gender indicators |
| **Economy** | Jobless growth, agrarian crisis, remittance dependency, 8-10M migrant workers |
| **Issues** | Naxal history, prohibition, health/education failure, water/sanitation |
| **People** | Ashoka to Karpoori Thakur, Bhikhari Thakur to Phanishwarnath Renu |
| **Food** | Litti chokha to makhana economics, caste on the plate, regional cuisines |
| **Culture** | Madhubani painting, Bidesia theatre, Chhath Puja, linguistic politics |
| **Performing Arts** | Bidesia, Jat-Jatin, Domkach, Sama-Chakeva, puppetry traditions |
| **Crafts** | 6 craft traditions with economics (maker price vs retail price) |
| **Climate** | Flood-drought cycle, Kosi embankment politics, heat stress, groundwater depletion |
| **Justice** | Naxal legacy, caste violence, prohibition enforcement, undertrial crisis |
| **Digital & Media** | WhatsApp politics, Bhojpuri YouTube, gender digital divide, DBT barriers |
| **Stories** | 45 perspective pieces -- makhana divers, child brides, ASHA workers, hooch deaths |
| **Data** | District indicator map, 12+ charts, Sankey & chord diagrams, Bihar vs India comparisons |
| **Tools** | 18 interactive tools (see below) |

## Tools (18)

- Surname Lookup -- caste category database (60+ entries)
- Bihar Lexicon -- searchable terms with etymology (Maithili, Bhojpuri, Magahi)
- District Data Explorer -- Census data for 20 districts
- Flood Risk Checker -- risk level and river systems (BSDMA data)
- Development Comparator -- multi-district chart generator
- Constituency Lookup -- 15 Lok Sabha seats, 2024 results, margins, caste profiles
- Issue Priority Ranker -- ranked local issues by district
- Scheme Gap Finder -- MGNREGA, PM-Kisan, Ujjwala coverage vs national average
- Reading List Generator -- 24 open-access sources, 8 topic filters
- Impact Calculator -- translates statistics into human terms
- Bihar Timeline -- 28 events from 600 BCE to 2024
- Voices of Bihar -- 20 published quotes, filterable by theme
- District One-Pager -- printable summary for fieldworkers
- Facilitator Guide -- 6 audience-specific listening circle session plans
- WhatsApp Fact Cards -- 12 pre-formatted Hindi messages, one-tap share
- District Briefing -- everything about one district on one page
- Bihar vs States -- compare Bihar against 9 states on 9 indicators
- District Indicator Map -- color-coded Bihar map by literacy, sex ratio, urbanisation, density

## Visualisations

- **12+ Chart.js charts** -- bar, line, doughnut, grouped comparisons
- **Migration flow Sankey** -- source districts → destination states → employment sectors (D3.js)
- **Budget pipeline Sankey** -- central allocation → scheme delivery with leakage at every stage (D3.js)
- **Caste-politics chord diagram** -- voting alignment between 7 caste groups and 5 political alliances (D3.js)
- **District indicator map** -- colour-coded Leaflet map (literacy, sex ratio, urbanisation, density)
- **Heritage sites map** -- 10 UNESCO/cultural sites with interactive markers
- **CSS flow diagrams** -- migration routes, cycle of deprivation, revenue flows, scheme delivery chain

## Features

- **Fully bilingual** -- all 17 sections translated EN/HI (Noto Serif Devanagari)
- **WhatsApp sharing** -- floating button + per-story share
- **Search** -- site-wide search across all content
- **Ctrl+K navigation** -- keyboard shortcuts for quick section access (1-9, S, D, T, R)
- **Light/Dark/Auto theme** -- 3-mode theme selector
- **Offline access** -- service worker caches the full site
- **PNG download** -- download any chart or D3 diagram with source watermark
- **Print** -- printable district briefings and one-pagers
- **Password protected** -- client-side access gate
- **Responsive** -- mobile-first CSS, works on all screen sizes

## Technology

Single HTML file. No build system. No framework.

- **Chart.js 3.9.1** -- bar, line, pie, doughnut charts
- **D3.js 7.8.5 + d3-sankey** -- Sankey and chord diagrams
- **Leaflet.js 1.9.4** -- interactive maps
- CSS-only flow diagrams (no Mermaid dependency)
- Noto Serif Devanagari for Hindi typography
- Newsreader + DM Sans + JetBrains Mono typography
- Service worker for full offline capability
- Hosted on Netlify (static site)

## Data Sources

All data is traceable to authenticated sources:

Census of India 2011 | NFHS-5 (2019-21) | Bihar Caste Survey 2023 | RBI Handbook of Statistics | Bihar Economic Survey | NITI Aayog MPI | ASER 2022 | ECI election data | BSDMA flood reports | CWC | NCRB | UNESCO | CPCB

Full bibliography with 45+ sources and open-access links in the References tab.

## Licence

MIT License. Content under CC BY 4.0.

---

*Bihar Parichay: because understanding a place means understanding its people, their problems, and who benefits from the solutions.*
