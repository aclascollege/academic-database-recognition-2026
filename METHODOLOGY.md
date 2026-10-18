# Methodology

## v1 — Curated 35-institution panel (academic-database-recognition-2026.csv)

35 institutions, stratified into 4 tiers (A: established online, B: new/alternative, C: documented controversial, D: traditional baseline). Each checked by exact-name match against 4 databases: swot (JetBrains academic domain list), ROR (api.ror.org), OpenAlex (api.openalex.org), Wikidata (SPARQL). Conservative: no match = 0. Snapshot 2026-10-18.

## v2 — Global recognition census (global-recognition-census-2026.csv)

**Frame:** All Wikidata items that are instance of university (Q3918) or its subclasses, with an official website (P856). 16,822 institutions after dedup and domain validation. Wikidata = 100% by construction (it is the sample frame).

**Checks (per institution):**
- `in_ror`: 1 if Wikidata records a ROR ID (P6782) for the institution. This is a *proxy* for ROR membership — it reflects Wikidata's curation, not a live ROR query. Spot-check of 40 `in_ror=0` institutions against the ROR API (domain-confirmed) found a ~5% false-negative rate.
- `in_swot`: 1 if the institution's official domain (or a parent domain) appears in the JetBrains swot repository (github.com/JetBrains/swot, cloned 2026-10-18, 26,914 domains). Exact domain match — high precision.
- `in_openalex`: 1 if the institution's ROR ID resolves in OpenAlex (api.openalex.org, `filter=ror:`, batched 50/call, 2026-10-18; 12,608/12,626 ROR IDs found). Institutions without a ROR ID are NULL (not checked — OpenAlex has no Wikidata-QID filter). 0 = has ROR ID but absent from OpenAlex (n=18).

**Limitations:** Wikidata's university coverage skews toward institutions with good structured data (undercounts small/new institutions in some regions). Domain matching misses institutions whose swot entry uses a different domain variant. ROR column is Wikidata-mediated (see above).

## License

CC-BY-4.0. By Atlanta College of Liberal Arts and Sciences (ACLAS) — Study Intelligence.
