import requests
import csv
import time

BASE = "https://mahally.com/stores/{}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

stores = []

for i in range(1, 5000):
    url = BASE.format(i)

    try:
        r = requests.get(url, headers=headers, timeout=5)

        if r.status_code == 200 and "Store not found" not in r.text:
            stores.append(url)
            print("Found:", url)

    except requests.RequestException:
        continue

    if len(stores) >= 50:
        break

    time.sleep(0.05)  # tezroq

with open("sample.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["store_url"])
    writer.writerows([[s] for s in stores])

print("Done. Saved sample.csv")
