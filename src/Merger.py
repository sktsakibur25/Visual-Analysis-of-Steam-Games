import os
import pandas as pd

csv_directory_path = "./ScrappedCSV/"

final_data = pd.DataFrame()

for item in os.listdir(csv_directory_path):
    if item.endswith('.csv'):
        file_path = os.path.join(csv_directory_path, item)
        df = pd.read_csv(file_path)
        final_data = pd.concat([final_data, df], ignore_index=True)

final_data.to_csv('GameData.csv', index=False)
