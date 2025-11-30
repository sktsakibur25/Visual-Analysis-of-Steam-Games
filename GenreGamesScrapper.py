import os
from bs4 import BeautifulSoup
import pandas as pd

directory_path = "./WebPages/"  
save_path = "./ScrappedCSV/"
file_list = []
for item in os.listdir(directory_path):
    full_path = os.path.join(directory_path, item)
    if os.path.isfile(full_path):
        file_list.append(item)

for filename in file_list:
    try:
        file_path = os.path.join(directory_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, 'html.parser')
            desired = ['Name', 'Price', 'Rating', 'Release', 'Follows', 'Online', 'Peak']
            genre_name = filename.replace(".html", "")

            tr = list(soup.find_all('tr', class_='app'))
            print(f"Processing {genre_name}, found {len(tr)} entries.")
            rows = []
            for r in tr:
                tds = r.find_all('td')
                if len(tds) < 10:
                    continue
                name = tds[2].get_text(strip=True)
                price = tds[4].get_text(strip=True)
                rating = tds[5].get_text(strip=True)
                release = tds[6].get_text(strip=True)
                follows = tds[7].get_text(strip=True)
                online = tds[8].get_text(strip=True)
                peak = tds[9].get_text(strip=True)

                rows.append({
                    'Name': name,
                    'Price': price,
                    'Rating': rating,
                    'Release': release,
                    'Follows': follows,
                    'Online': online,
                    'Peak': peak,
                    'Genre': genre_name
                })

            if rows:
                df = pd.DataFrame(rows, columns=['Name','Price','Rating','Release','Follows','Online','Peak','Genre'])
                csv_filename = f"{genre_name}.csv"
                df.to_csv(str(save_path+csv_filename), index=False, encoding='utf-8-sig')

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")