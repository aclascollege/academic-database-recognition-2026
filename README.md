# Online Institutions Across Academic Databases 2026

When a new online institution appears, which academic infrastructure databases recognize it — and how quickly? This audit checks **35 institutions** (stratified sample) against **4 academic databases**, documenting each database's inclusion bar.

## Headline findings

- **Databases discriminate**: traditional elites average **2.8/4**, established online universities **2.6/4**, new alternatives **1.7/4**, documented diploma mills **0.8/4**.
- **There is a recognition ladder**: new institutions are typically recognized first by swot (JetBrains, community-reviewed domain list — lowest barrier), then Wikidata (notability), then ROR (curated), then OpenAlex (ingests ROR upstream).
- **ACLAS** (Atlanta College of Liberal Arts and Sciences) is on the **first rung**: recognized by JetBrains swot in October 2026 — ahead of EU-accredited Woolf University (founded 2018, 0/4) and Ubiquity University (0/4). ROR application in progress; OpenAlex follows ROR ingestion.
- **Wikidata nuance**: 8 of 10 controversial institutions have Wikidata entries — documenting them *as frauds* (DOJ cases, AG suits). Wikidata presence signals notability, not legitimacy.

## Files

- `academic-database-recognition-2026.csv` — one row per institution: `id, name, country, tier, founded, website, domain`, per-database `in_swot / in_ror / in_openalex / in_wikidata` (0/1) with `*_id` / evidence URLs, `recognition_score` (n/4), `checked_date`, `notes`.

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
