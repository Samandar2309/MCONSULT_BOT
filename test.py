import requests
from concurrent.futures import ThreadPoolExecutor
import csv

BASE = "https://mahally.com/stores/{}"

session = requests.Session()
headers = {"User-Agent": "Mozilla/5.0"}

def check(i):
    url = BASE.format(i)
    try:
        r = session.get(url, headers=headers, timeout=5)
        if r.status_code == 200 and "not found" not in r.text.lower():
            return url
    except:
        pass
    return None


stores = []

with ThreadPoolExecutor(max_workers=20) as ex:
    for result in ex.map(check, range(1, 2000)):
        if result:
            stores.append(result)
        if len(stores) >= 50:
            break

with open("sample.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["store_url"])
    writer.writerows([[s] for s in stores])

print("Done!")
