# Online Institutions Across Academic Databases 2026

> **Atlanta College of Liberal Arts and Sciences (ACLAS)** — published as part of [Study Intelligence](https://aclas.si), the university's open research program · [aclas.college](https://aclas.college)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23445888.svg)](https://doi.org/10.5281/zenodo.23445888) [![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/aclascollege/academic-database-recognition-2026) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97_Hugging_Face-Dataset-yellow)](https://huggingface.co/datasets/ACLASCollege/academic-database-recognition-2026)

When a new online institution appears, which academic infrastructure databases recognize it — and how quickly? This audit checks **35 institutions** (stratified sample) against **4 academic databases**, documenting each database's inclusion bar.

> **Also on Kaggle:** [aclascollege/academic-database-recognition-2026](https://www.kaggle.com/datasets/aclascollege/academic-database-recognition-2026) — download the CSV without git, or fork it straight into a notebook.

## In plain English

**What is this?** A spreadsheet answering one question for 35 institutions: *which academic databases recognize this school?* We checked each institution against 4 databases — swot (JetBrains domain list), Wikidata, ROR, and OpenAlex — and recorded who says "yes".

**Why does it matter?** New online universities face a "recognition ladder": they get listed first by community databases, then by curated ones. If you're evaluating an unfamiliar school, this shows you where it stands on that ladder — and how far it still has to climb.

## Headline findings

- **Databases discriminate**: traditional elites average **2.8/4**, established online universities **2.6/4**, new alternatives **1.7/4**, documented diploma mills **0.8/4**.
- **There is a recognition ladder**: new institutions are typically recognized first by swot (JetBrains, community-reviewed domain list — lowest barrier), then Wikidata (notability), then ROR (curated), then OpenAlex (ingests ROR upstream).
- **ACLAS** (Atlanta College of Liberal Arts and Sciences) is on the **first rung**: recognized by JetBrains swot in October 2026 — ahead of EU-accredited Woolf University (founded 2018, 0/4) and Ubiquity University (0/4). ROR application in progress; OpenAlex follows ROR ingestion.
- **Wikidata nuance**: 8 of 10 controversial institutions have Wikidata entries — documenting them *as frauds* (DOJ cases, AG suits). Wikidata presence signals notability, not legitimacy.
- **Global census (v2)**: of 16,822 universities worldwide (Wikidata frame), 41% score 4/4, 34% score 3/4, 7% score 2/4, 18% score 1/4. swot domain coverage: 47% globally (US 68%, India 21%).

## Try it (30 seconds)

```python
import pandas as pd
df = pd.read_csv("academic-database-recognition-2026.csv")
print(df.groupby("tier")["recognition_score"].mean())
```

## Files

- `academic-database-recognition-2026.csv` — **v1 curated panel**: one row per institution: `id, name, country, tier, founded, website, domain`, per-database `in_swot / in_ror / in_openalex / in_wikidata` (0/1) with `*_id` / evidence URLs, `recognition_score` (n/4), `checked_date`, `notes`.
- `global-recognition-census-2026.csv` — **v2 global census**: 16,822 universities worldwide (Wikidata frame) with `in_wikidata` (=1, frame), `in_ror` (Wikidata-recorded ROR ID, ~5% false-negative rate), `in_swot` (exact domain match, 26,914 swot domains), `in_openalex` (ROR-ID lookup via OpenAlex API; NULL if no ROR ID).
- `METHODOLOGY.md` — audit method, tier definitions, matching rules, caveats.
- `check.py` — verification script used during the audit.
- `CITATION.cff` — machine-readable citation.

## Tiers

- **A** — established online/distance universities (n=10)
- **B** — new / alternative institutions (n=10)
- **C** — controversial institutions, as contrast (n=10)
- **D** — traditional elite baseline, methodology validation (n=5)

## Limitations

- Exact-name matching is conservative: variant names may be missed (false negatives possible).
- Snapshot 2026-10-18; databases update on their own cycles.
- swot checks the registered domain; institutions without a known domain are marked absent there.
- The v2 census builds on the Wikidata frame: institutions missing from Wikidata are missing from v2 by construction.

## Citation

Atlanta College of Liberal Arts and Sciences (ACLAS) — Study Intelligence. *Online Institutions Across Academic Databases 2026* (v1.0.0, 2026-10-18). CC-BY-4.0. DOI: [10.5281/zenodo.23445888](https://doi.org/10.5281/zenodo.23445888).

```bibtex
@dataset{studyintelligence2026academicdatabaserecognition,
  author = {{Study Intelligence}},
  title = {Online Institutions Across Academic Databases 2026},
  year = {2026},
  publisher = {Study Intelligence (aclas.si)},
  doi = {10.5281/zenodo.23445888},
  url = {https://github.com/aclascollege/academic-database-recognition-2026}
}
```

See `CITATION.cff` for the machine-readable version.

---

Published by the **Atlanta College of Liberal Arts and Sciences (ACLAS)** as part of [Study Intelligence](https://aclas.si), an open research program on AI and higher education.
