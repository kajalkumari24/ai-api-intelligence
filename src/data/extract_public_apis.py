import re
import requests
import pandas as pd
from pathlib import Path

README_URL = "https://raw.githubusercontent.com/public-apis/public-apis/master/README.md"
OUTPUT_PATH = Path("data/raw/public_apis_raw.csv")

ROW_PATTERN = re.compile(
    r"^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"
)
CATEGORY_PATTERN = re.compile(r"^### (.+)")


def fetch_readme(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def parse_readme(markdown_text: str) -> pd.DataFrame:
    records = []
    current_category = None

    for line in markdown_text.splitlines():
        category_match = CATEGORY_PATTERN.match(line)
        if category_match:
            current_category = category_match.group(1).strip()
            continue

        row_match = ROW_PATTERN.match(line)
        if row_match and current_category:
            name, link, description, auth, https, cors = row_match.groups()
            records.append({
                "name": name.strip(),
                "description": description.strip(),
                "category": current_category,
                "auth": auth.strip(),
                "https": https.strip(),
                "cors": cors.strip(),
                "link": link.strip(),
            })

    return pd.DataFrame(records)


def main():
    print("Fetching README...")
    markdown_text = fetch_readme(README_URL)

    print("Parsing table rows...")
    df = parse_readme(markdown_text)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved {len(df)} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()