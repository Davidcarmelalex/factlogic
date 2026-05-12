# FactLogic

> Evidence beats belief. Every time.

[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](LICENSE)
[![Next.js](https://img.shields.io/badge/Next.js-16-black)](https://nextjs.org)
[![Part of](https://img.shields.io/badge/FCRI-Research-gold)](https://fcri.science)

**FactLogic** is the ultimate myth-busting engine — separating scientific evidence from misinformation through rigorous critical analysis and clear logical reasoning.

Every claim gets a verdict. Every verdict gets its evidence.

---

## Verdict System

| Verdict | Meaning |
|---------|---------|
| ✅ TRUE | Supported by strong scientific consensus |
| ❌ FALSE | Contradicted by evidence |
| ⚠️ MISLEADING | Contains truth but distorts context |
| 🔬 NUANCED | Partially true — context matters |
| ❓ UNVERIFIED | Insufficient evidence to conclude |

---

## Architecture

```
factlogic/
├── src/app/
│   ├── page.tsx           Featured myths + search
│   ├── myth/[slug]/       Full myth investigation
│   ├── categories/        Browse by category
│   ├── submit/            Community myth submissions
│   └── methodology/       How we investigate
├── agents/
│   └── investigator.py    AI myth investigation agent
├── lib/
│   └── evidence.ts        Evidence scoring utilities
└── tests/
```

---

## Investigation Process

```
Claim submitted → Agent searches literature
    → Evidence collected and scored
    → Logic score (0–10) + Science score (0–10)
    → Human review (optional)
    → Verdict published with full reasoning
```

---

## Stack

Next.js 16 · TypeScript · Tailwind CSS 4 · Python investigation agent · PostgreSQL

---

## Quick Start

```bash
git clone https://github.com/Davidcarmelalex/factlogic
cd factlogic && npm install && cp .env.example .env.local && npm run dev
```
