import pandas as pd

mapeamento={
    'codigo_ativo': 'int32',
    'nome_ativo': 'string',
    'codigo_segmento': 'int32'
}

df1 = pd.read_csv(r'C:\Users\mapo_\Projetos\pandas\v1.csv', dtype=mapeamento, delimiter=';')
df2 = pd.read_csv(r'C:\Users\mapo_\Projetos\pandas\v2.csv', dtype=mapeamento, delimiter=';')

df3 = pd.merge(df1, df2, how='outer', on=['codigo_ativo','nome_ativo','codigo_segmento'])
df4 = df3.drop_duplicates(subset=['codigo_ativo'], keep='last')

print(df4)