<div align="center">

# **FactLogic**

### *The Truth Doesn't Negotiate — Evidence-Based Myth Busting*

[![Status](https://img.shields.io/badge/Status-Building-ff6600?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-0f0f0f?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-3776ab?style=flat-square&logo=python&logoColor=white)]()
[![Next.js](https://img.shields.io/badge/Next.js-16-000000?style=flat-square&logo=next.js&logoColor=white)]()

**If it cannot survive scrutiny, it was never a fact.**

[Pipeline](#pipeline) · [Methodology](#methodology) · [Quick Start](#quick-start) · [Ecosystem](#ecosystem)

</div>

---

## What is FactLogic?

FactLogic is an ultimate myth-busting engine that separates scientific evidence from misinformation through critical analysis. It uses AI to cross-reference claims against peer-reviewed research, authoritative databases, and verified sources.

## Pipeline

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  CLAIM   │───▶│  SEARCH  │───▶│ EVALUATE │───▶│  VERDICT │
│  INPUT   │    │  SOURCES │    │ EVIDENCE │    │  OUTPUT  │
│          │    │          │    │          │    │          │
│ - Text   │    │ - PubMed │    │ - Study  │    │ - True   │
│ - URL    │    │ - ArXiv  │    │   quality│    │ - False  │
│ - Image  │    │ - Wiki   │    │ - Sample │    │ - Partial│
│          │    │ - News   │    │   size   │    │ - Unknown│
└──────────┘    └──────────┘    └──────────┘    └──────────┘
```

## Methodology

| Verdict | Criteria |
|---------|----------|
| **True** | Multiple peer-reviewed sources confirm |
| **Partially True** | Some evidence supports, with important caveats |
| **False** | Contradicted by reliable evidence |
| **Unverifiable** | Insufficient evidence to assess |

## Features

| Feature | Status | Description |
|---------|--------|-------------|
| **Claim Extraction** | 🚧 Building | NLP-based claim identification |
| **Source Search** | 🚧 Building | Automated evidence retrieval |
| **Evidence Scoring** | 🚧 Building | Study quality and relevance ranking |
| **Visual Fact-Check** | 📋 Planned | Image claim verification |
| **Trend Analysis** | 📋 Planned | Misinformation pattern detection |
| **API Access** | 📋 Planned | Programmatic fact-checking |

## Tech Stack

- **Frontend:** Next.js 16 · TypeScript · Tailwind CSS
- **NLP:** Python · spaCy · transformers
- **Search:** SerpAPI · PubMed API · CrossRef
- **ML:** scikit-learn · Evidence classification model

## Quick Start

```bash
git clone https://github.com/Davidcarmelalex/factlogic.git
cd factlogic

# Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Frontend
cd ../web
npm install
npm run dev        # http://localhost:3000
```

## Ecosystem

FactLogic is part of the **M&R&Nothing** ecosystem:

- Powers **VOID//SIGNAL** fact-check layer
- Integrates with **Nexum Labs** for educational content verification
- Supports **Jan Niti** public claim analysis

→ [github.com/Davidcarmelalex/MrNothingEcosystem](https://github.com/Davidcarmelalex/MrNothingEcosystem)

---

*Separating signal from noise.*
*MR° · M&R&Nothing · 2026 · A tribute, by David Carmel Alex*
