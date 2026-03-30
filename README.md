# Bihar Parichay
*A Comprehensive Academic Deep Dive into Bihar*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Academic Resource](https://img.shields.io/badge/purpose-academic%20resource-green.svg)]()
[![Static Site](https://img.shields.io/badge/deploy-Netlify-blue.svg)]()

## Overview

Bihar Parichay (Bihar -- "Introduction") is an academic deep-dive resource providing comprehensive, data-driven analysis of Bihar, India. The site covers geography, demographics, economy, social issues, people, food, art and culture -- all with interactive visualisations and links to authenticated open-access scholarly sources.

Built as a single-page static site, it is designed for researchers, students, policy professionals, and anyone seeking a rigorous introduction to one of India's most historically significant and complex states.

## Sections

| Section | Description |
|---------|-------------|
| **Overview** | Key facts, historical context, and state profile |
| **Geography & Maps** | Interactive Leaflet map, rivers, administrative divisions |
| **Demographics & Society** | Population, caste structure, religion, literacy, urbanisation |
| **Economy & Development** | GSDP trends, sectoral composition, agriculture, migration economy |
| **Social Issues** | Poverty (MPI), floods, health (NFHS-5), education, gender |
| **Notable People** | Historical figures, freedom movement leaders, intellectuals |
| **Food & Cuisine** | Regional culinary traditions, signature dishes, agricultural connections |
| **Art, Culture & Heritage** | Madhubani painting, UNESCO sites, performing arts, languages |
| **Data & Analysis** | Interactive Chart.js dashboards, radar charts, heritage map |
| **References** | 25+ authenticated open-access academic sources |

## Technology

- **Single-file architecture**: Everything in `index.html` (HTML + CSS + JS)
- **Chart.js 3.9**: Interactive data visualisations (bar, line, radar, doughnut, pie)
- **Leaflet.js 1.9**: Interactive maps with OpenStreetMap tiles
- **Fonts**: Inter, Merriweather, Noto Serif Devanagari
- **No build system**: Deploy directly to any static hosting service
- **Password-protected**: Client-side SHA-256 gate for restricted access

## Deployment

The site deploys as a static single HTML file on Netlify (or any static host):

```bash
# Clone and deploy
git clone https://github.com/Varnasr/BiharParichay-Project.git
# Upload index.html to Netlify, Vercel, GitHub Pages, or open locally
```

## Data Sources

All data is sourced from authenticated open-access publications:

- Census of India 2011
- National Family Health Survey 5 (NFHS-5, 2019-21)
- Bihar Economic Survey 2022-23
- RBI Handbook of Statistics on Indian States
- NITI Aayog Multidimensional Poverty Index
- ASER 2022 (Annual Status of Education Report)
- UNESCO World Heritage entries (Nalanda, Bodh Gaya)
- World Bank Bihar Development Reports

Full bibliography with direct links is available in the References section of the site.

## Academic Citation

```bibtex
@misc{bihar_parichay_2025,
  title={Bihar Parichay: A Comprehensive Academic Deep Dive into Bihar},
  author={Raman, Varna Sri},
  year={2025},
  url={https://github.com/Varnasr/BiharParichay-Project},
  note={Interactive academic resource on Bihar's geography, society, economy, and culture}
}
```

## Legal & Ethical Guidelines

- **Academic use only**: Designed for research and educational purposes
- **MIT License**: Open source with attribution
- **CC BY 4.0**: Content provided under Creative Commons Attribution 4.0
- **Data accuracy**: All efforts made to cite reliable sources; no warranties provided
- **Non-partisan**: Content is factual and balanced

## Contributing

Contributions welcome -- particularly:
- Corrections to data or citations
- Additional authenticated academic sources
- Accessibility improvements
- Translations (Hindi, Maithili, Bhojpuri)

## Version History

- **v3.0** (2025): Complete redesign as academic deep-dive site with interactive maps, charts, and 10 content sections
- **v2.0**: Web-based demographic classification tool
- **v1.0**: Initial release with core classification functionality

---

*Bihar Parichay: An open-access academic resource for understanding Bihar's society, economy, geography, and culture.*
