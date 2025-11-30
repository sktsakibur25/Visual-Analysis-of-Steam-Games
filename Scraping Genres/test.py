import pandas as pd
import os

# Check current directory and use full path if needed
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'genre.csv'))

print(df['tag_name'].unique())