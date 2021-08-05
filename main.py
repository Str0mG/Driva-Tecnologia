import pandas as pd

df = pd.read_csv('DadosEmpresa.csv')  #Leitura

for i in range(df.shape[1]):
    print(f'{i+1}-{df.columns[i]}')  #Apresentação das colunas

print(df.head()) #Primeiras linhas

print("\nTotal de Sim em Opcao_pelo_simples: ", df.loc[df.opcao_pelo_simples == 'SIM'].shape[0])
print("Total de capital social:", df['capital_social'].sum())

print(df[(df['capital_social'] > 10000) & (df['capital_social'] < 20000)])

df2 = pd.read_csv('DadosEndereco.csv')

new_df = pd.merge(df, df2)

new_df[new_df['municipio']=='CURITIBA'].to_csv('novo.csv')
