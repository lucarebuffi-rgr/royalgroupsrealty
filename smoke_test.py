"""Pre-deploy smoke test for the royalgroupsrealty Flask app.

Run BEFORE every deploy: python3 smoke_test.py
Catches: missing imports, type errors in template helpers, broken routes,
         mobile/desktop template selection, og-tag rendering.

Mocks get_all_deals() so no Firestore quota is touched.
"""
import importlib.util
import os
import sys

SITE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("rgr_app", os.path.join(SITE, "app.py"))
app_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_mod)
app = app_mod.app

SAMPLE_DEALS = [
    {"_id": "abc123", "address": "63 S Villa Rd", "city": "Villa Rica", "state": "GA",
     "zip": "30180", "askPrice": 35000, "arv": 180000, "repairEst": 50000,
     "beds": "3", "baths": "2", "sqft": 1400, "headline": "Great flip in Villa Rica",
     "notes": "Needs work.\nPriced to move.", "stage": "active",
     "masterPhoto": "https://example.com/photo.jpg",
     "driveFolderUrl": "https://drive.google.com/drive/folders/xyz",
     "createdAt": "2026-10-17T00:00:00Z"},
    {"_id": "def456", "address": "1804 South Dr", "city": "Venus", "state": "TX",
     "zip": "76084", "askPrice": 120000, "arv": 210000, "stage": "active",
     "createdAt": "2026-10-16T00:00:00Z"},
]

app_mod.get_all_deals = lambda: SAMPLE_DEALS
DESKTOP_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36"
MOBILE_UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
             "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")

failures = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (" — " + detail if detail and not cond else ""))
    if not cond:
        failures.append(name)


client = app.test_client()

# 0. manual rent override (DispoHub rentLow/rentHigh) beats cache + RentCast
ov = app_mod.get_rent_estimate({"propertyType": "Single Family", "rentLow": 1100, "rentHigh": 1200, "_id": "t1"})
check("rent override returns midpoint + range", ov == (1150, 1100, 1200), f"got {ov}")
ov_land = app_mod.get_rent_estimate({"propertyType": "Land", "rentLow": 1100, "rentHigh": 1200, "_id": "t2"})
check("rent override ignored on land-only", ov_land == (None, None, None), f"got {ov_land}")

# 1. deals index — desktop + mobile
r = client.get("/deals", headers={"User-Agent": DESKTOP_UA})
check("GET /deals desktop 200", r.status_code == 200, f"got {r.status_code}")
r = client.get("/deals", headers={"User-Agent": MOBILE_UA})
check("GET /deals mobile 200", r.status_code == 200, f"got {r.status_code}")
check("mobile /deals serves mobile template", b"viewport-fit=cover" in r.data)

# 2. API list
r = client.get("/api/deals")
check("GET /api/deals 200 + 2 deals", r.status_code == 200 and len(r.get_json()) == 2,
      f"got {r.status_code}")

# 3. single-deal API by slug and by id (this caught the missing `import re`)
for key in ("63SVillaRd", "abc123"):
    r = client.get(f"/api/deal/{key}")
    ok = r.status_code == 200 and r.get_json().get("_id") == "abc123"
    check(f"GET /api/deal/{key} 200", ok, f"got {r.status_code}")

# 4. deal pages — desktop + mobile, og tags present (this caught the "$" + int crash)
for ua, label, mobile_marker in ((DESKTOP_UA, "desktop", None), (MOBILE_UA, "mobile", b"sticky-bar")):
    r = client.get("/63SVillaRd", headers={"User-Agent": ua})
    check(f"GET /63SVillaRd {label} 200", r.status_code == 200, f"got {r.status_code}")
    if r.status_code == 200:
        check(f"og:title present ({label})", b'property="og:title"' in r.data)
        check(f"og:description present ({label})", b'property="og:description"' in r.data)
        check(f"og:image absent ({label})", b'property="og:image"' not in r.data)
        if mobile_marker:
            check("mobile template has sticky bar", mobile_marker in r.data)
    r = client.get("/deals/abc123", headers={"User-Agent": ua})
    check(f"GET /deals/abc123 {label} 200", r.status_code == 200, f"got {r.status_code}")

# 4b. og-image route returns a PNG
r = client.get("/og-image/63SVillaRd")
check("GET /og-image/63SVillaRd PNG", r.status_code == 200 and r.content_type == "image/png",
      f"got {r.status_code} {r.content_type}")

# 5. unknown slug: API 404s; page renders and client shows "not found" (by design)
r = client.get("/api/deal/no-such-deal-xyz")
check("GET /api/deal/no-such-deal-xyz 404", r.status_code == 404, f"got {r.status_code}")
r = client.get("/no-such-deal-xyz")
check("GET /no-such-deal-xyz renders (client shows not-found)",
      r.status_code == 200 and b"deal-root" in r.data, f"got {r.status_code}")

print()
if failures:
    print(f"{len(failures)} FAILURES — do not deploy")
    sys.exit(1)
print("All smoke tests passed — safe to deploy")
