from pathlib import Path
import pandas as pd
import requests

url = "https://api.openalex.org/works"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "openalex_hydrogels.csv"

params = {
    "search": "hydrogel",
    "per_page": 100
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

data = response.json()

articles = []

for article in data["results"]:
    articles.append({
        "title": article["title"],
        "year": article["publication_year"],
        "doi": article["doi"],
        "citations": article["cited_by_count"],
        "open_access": article["open_access"]["is_oa"],
        "type": article["type"]
    })

df = pd.DataFrame(articles)

print(df.head(10).to_string(index=False))
print(df.shape)

df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")