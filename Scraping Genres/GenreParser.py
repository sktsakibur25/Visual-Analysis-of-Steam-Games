import pandas as pd


df = pd.read_csv('tags.csv')

puzzle_idx = df[df['tag_name'] == 'Puzzle'].index[0]
trivia_idx = df[df['tag_name'] == 'Trivia'].index[0]

filtered_df = df.iloc[puzzle_idx:trivia_idx]

# filtered_df.to_csv('genre.csv', index=False)
