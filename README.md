# Online Institutions Across Academic Databases 2026

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23445888.svg)](https://doi.org/10.5281/zenodo.23445888) [![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/aclascollege/academic-database-recognition-2026) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97_Hugging_Face-Dataset-yellow)](https://huggingface.co/datasets/ACLASCollege/academic-database-recognition-2026)

When a new online institution appears, which academic infrastructure databases recognize it — and how quickly? This audit checks institutions against **4 academic databases** (swot, ROR, OpenAlex, Wikidata), documenting each database's inclusion bar: a **v1 curated panel of 35 institutions** (stratified sample) plus a **v2 global census of 16,822 universities** worldwide.

## Headline findings

- **Databases discriminate**: traditional elites average **2.8/4**, established online universities **2.6/4**, new alternatives **1.7/4**, documented diploma mills **0.8/4**.
- **There is a recognition ladder**: new institutions are typically recognized first by swot (JetBrains, community-reviewed domain list — lowest barrier), then Wikidata (notability), then ROR (curated), then OpenAlex (ingests ROR upstream).
- **ACLAS** (Atlanta College of Liberal Arts and Sciences) is on the **first rung**: recognized by JetBrains swot in October 2026 — ahead of EU-accredited Woolf University (founded 2018, 0/4) and Ubiquity University (0/4). ROR application in progress; OpenAlex follows ROR ingestion.
- **Wikidata nuance**: 8 of 10 controversial institutions have Wikidata entries — documenting them *as frauds* (DOJ cases, AG suits). Wikidata presence signals notability, not legitimacy.

## Files

- `academic-database-recognition-2026.csv` — **v1 curated panel**: one row per institution: `id, name, country, tier, founded, website, domain`, per-database `in_swot / in_ror / in_openalex / in_wikidata` (0/1) with `*_id` / evidence URLs, `recognition_score` (n/4), `checked_date`, `notes`.
- `global-recognition-census-2026.csv` — **v2 global census**: 16,822 universities worldwide (Wikidata frame) with `in_wikidata` (=1, frame), `in_ror` (Wikidata-recorded ROR ID, ~5% false-negative rate), `in_swot` (exact domain match, 26,914 swot domains), `in_openalex` (ROR-ID lookup via OpenAlex API; NULL if no ROR ID). Score distribution: 4/4: 6,817 (41%), 3/4: 5,801 (34%), 2/4: 1,109 (7%), 1/4: 3,095 (18%). swot coverage: 47% globally (US 68%, India 21%).

## Tiers

- **A** — established online/distance universities (n=10)
- **B** — new / alternative institutions (n=10)
- **C** — controversial institutions, as contrast (n=10)
- **D** — traditional elite baseline, methodology validation (n=5)

## Limitations

- Exact-name matching is conservative: variant names may be missed (false negatives possible).
- Snapshot 2026-10-18; databases update on their own cycles.
- swot checks the registered domain; institutions without a known domain are marked absent there.

## Citation

Atlanta College of Liberal Arts and Sciences (ACLAS) — Study Intelligence. *Online Institutions Across Academic Databases 2026*. CC-BY-4.0.
