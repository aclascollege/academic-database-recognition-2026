# Methodology — Online Institutions Across Academic Databases 2026

## Research question

When a new online institution appears, which academic infrastructure databases recognize it,
and how quickly? This audit checks a stratified sample of 35 institutions against four
academic databases, documenting each database's inclusion criteria.

## Sample frame (n=35, stratified)

| Tier | Description | n |
|------|-------------|---|
| A | Established online/distance universities | 10 |
| B | New / alternative institutions (founded ~2005+) | 10 |
| C | Controversial institutions (documented diploma mills, as contrast) | 10 |
| D | Traditional elite baseline (methodology validation — expected 4/4) | 5 |

Tier C is included as a **contrast group**: if the databases could not discriminate
between tier A and tier C, that would itself be a finding.

## Databases and inclusion criteria

| Database | What it is | Inclusion bar | Check method |
|----------|-----------|---------------|--------------|
| **swot** (JetBrains) | Community-maintained academic domain list, used for educational-license verification | Domain looks like a legitimate educational institution (PR reviewed by maintainers) | `lib/domains/<tld>/<sld>.txt` exists in JetBrains/swot |
| **ROR** | Research Organization Registry — persistent IDs for research orgs | Org conducts/funds/publishes research; curation review (4–6 weeks) | api.ror.org exact name match |
| **OpenAlex** | Open scholarly index (ingests ROR) | Presence in upstream sources (ROR, MAG, Crossref) | api.openalex.org/institutions exact name match |
| **Wikidata** | Community knowledge base | Notability + volunteer curation | wbsearchentities exact label match |

## Fields

- `in_swot / in_ror / in_openalex / in_wikidata` — boolean presence
- `*_id` / `swot_evidence` — the matched identifier or evidence URL
- `checked_date` — snapshot date (2026-10-18); databases change

## Limitations

- Exact-name matching is conservative: an institution present under a variant name
  may be missed (false negatives possible; false positives unlikely).
- swot checks the registered domain; institutions without a known domain are marked absent.
- This is a snapshot. ROR/OpenAlex ingest on their own cycles.

## Headline pattern (to verify against data)

Established institutions cluster at 3–4/4 databases; controversial institutions at 0/4;
new alternatives are in transition — typically recognized first by the lowest-barrier
database (swot), with ROR/OpenAlex following after curation.
