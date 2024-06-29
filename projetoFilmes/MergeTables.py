import pandas as pd

tsv1 = pd.read_csv("title.ratings.tsv", sep='\t')
tsv2 = pd.read_csv("title.basics.tsv", sep='\t', low_memory=False)

tsv1['tconst'] = tsv1['tconst'].str.extract(r'(\d+)').astype(int)
tsv2['tconst'] = tsv2['tconst'].str.extract(r'(\d+)').astype(int)

df = pd.merge(tsv1, tsv2, on='tconst')

df = df.drop(columns=['originalTitle', 'runtimeMinutes', 'endYear', 'isAdult'])

df['genres'] = df['genres'].apply(lambda x: x.split(',')[0] if pd.notnull(x) and x != r'\N' else 'Sem Classificação')

df = df[df['titleType'].isin(['movie', 'tvSeries'])]

df = df.sort_values(by='tconst').reset_index(drop=True)
df['tconst'] = df.index + 1

df.to_csv("combined_titles.csv", sep='\t', index=False)
