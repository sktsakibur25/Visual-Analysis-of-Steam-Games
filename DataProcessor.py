import pandas as pd

df = pd.read_csv('GameData.csv')

# Print rows where any value is "—"
# rows_with_dash = df[(df['Follows'] == '—') | (df['Online'] == '—') | (df['Peak'] == '—') | (df['Price'] == '—')]
# print(f"Row count: {len(rows_with_dash)}")
# print(rows_with_dash)

df.replace('—', "N/A", inplace=True)
df = df[(df['Price'] != 'N/A') & (df['Rating'] != 'N/A') & (df['Follows'] != 'N/A') & (df['Peak'] != 'N/A') & (df['Release'] != 'N/A') & (df['Online'] != 'N/A')]

df['Price'] = df['Price'].replace('Free', '0')
df['Price'] = df['Price'].str.replace('$', '').astype(float).round(2)
df['Rating'] = df['Rating'].str.replace("%","").astype(float).round(2)

df['Follows'] = df['Follows'].str.replace(',', '').astype(int)
df['Peak'] = df['Peak'].str.replace(',', '').astype(int)
df['Online'] = df['Online'].str.replace(',', '').astype(int)

df['Release'] = df['Release'].str[-4:]

df.to_excel('ProcessedGameData.xlsx', index=False)