import pandas as pd

data = pd.read_csv('combined_titles.csv', sep='\t', low_memory=False)

data.to_csv('tabela_filmes.csv', index=False)