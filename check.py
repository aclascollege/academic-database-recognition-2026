"""Pilot checker: institution presence across swot / ROR / OpenAlex / Wikidata."""
import urllib.request, urllib.parse, json, time

def get(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ACLAS-Study-Intelligence/1.0"})
        return json.load(urllib.request.urlopen(req, timeout=timeout))
    except Exception as e:
        return {"_error": str(e)[:80]}

def check_swot(domain):
    # swot layout: lib/domains/<tld>/<sld>.txt  (multi-level tlds handled loosely)
    parts = domain.split(".")
    for tld_len in (1, 2):
        if len(parts) <= tld_len: continue
        tld = ".".join(parts[-tld_len:])
        sld = parts[-tld_len-1]
        url = f"https://raw.githubusercontent.com/JetBrains/swot/master/lib/domains/{tld}/{sld}.txt"
        try:
            urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "x"}), timeout=15)
            return True, url
        except Exception:
            continue
    return False, ""

def check_ror(name):
    q = urllib.parse.quote(name)
    d = get(f"https://api.ror.org/organizations?query={q}")
    target = name.lower()
    for x in d.get("items", []):
        vals = [n.get("value", "").lower() for n in x.get("names", [])]
        if any(v == target for v in vals):
            return True, x["id"]
    return False, ""

def check_openalex(name):
    q = urllib.parse.quote(name)
    d = get(f"https://api.openalex.org/institutions?search={q}&per-page=5")
    target = name.lower()
    for x in d.get("results", []):
        if x.get("display_name", "").lower() == target:
            return True, x["id"]
    return False, ""

def check_wikidata(name):
    q = urllib.parse.quote(name)
    d = get(f"https://www.wikidata.org/w/api.php?action=wbsearchentities&search={q}&language=en&format=json&type=item&limit=10")
    target = name.lower()
    for x in d.get("search", []):
        if x.get("label", "").lower() == target:
            return True, f"https://www.wikidata.org/wiki/{x['id']}"
    return False, ""

if __name__ == "__main__":
    import sys
    data = json.load(open(sys.argv[1]))
    out = []
    for row in data:
        name, domain = row["name"], row["domain"]
        sw, sw_e = check_swot(domain); time.sleep(0.3)
        rr, rr_e = check_ror(name); time.sleep(0.3)
        oa, oa_e = check_openalex(name); time.sleep(0.3)
        wd, wd_e = check_wikidata(name); time.sleep(0.3)
        out.append({**row, "in_swot": sw, "swot_evidence": sw_e,
                    "in_ror": rr, "ror_id": rr_e,
                    "in_openalex": oa, "openalex_id": oa_e,
                    "in_wikidata": wd, "wikidata_id": wd_e})
        print(f"{row['id']}: swot={sw} ror={rr} oa={oa} wd={wd}", flush=True)
    json.dump(out, open(sys.argv[2], "w"), indent=1)
    print("saved", sys.argv[2])
