from bs4 import BeautifulSoup
import csv
import re
from pathlib import Path

file_path = Path(__file__).with_name("Steam Tags.html")
output_csv = Path(__file__).with_name("tags.csv")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, 'html.parser')

    labels = soup.find_all('div', class_='label')
    rows = []

    for lbl in labels:
        a = lbl.find('a')
        if not a:
            continue

        url = a.get('href', '').strip()

        # Try to get the visible tag name (text node after emoji span)
        texts = [t.strip() for t in a.find_all(string=True, recursive=False) if t.strip()]
        if texts:
            tag_name = texts[-1]
        else:
            tag_name = a.get_text(strip=True)
            # remove leading non-alphanumeric characters (emoji, punctuation)
            tag_name = re.sub(r'^[^\w0-9\'"\-&]+', '', tag_name)

        count_span = lbl.find('span', class_='label-count')
        game_count = count_span.get_text(strip=True) if count_span else ''

        rows.append((tag_name, url, game_count))

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['tag_name', 'url', 'game_count'])
        writer.writerows(rows)

    print(f"Wrote {len(rows)} tags to {output_csv}")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")