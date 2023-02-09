import pandas as pd

dados = {
    'Nome':['Hilster',
            ['Carlos','Henrique'],
            ['Carlos','Alessandro'],
            'Talia',
            ['Bruno','Luan'],
            'Rafaela'],
    'Sobrenome':[['Barbosa','Santos'],
                 ['Carvalho','Ferreira'],
                 ['Fernandes','de Oliveira'],
                 ['Rodrigues','Costa'],
                 ['Pereira','da Silva'],
                 ['Barbosa','Cardoso']
                 ],
    'Idade':[21,
             50,
             21,
             20,
             22,
             18],
    'Sexo':['M',
            'M',
            'M',
            'F',
            'M',
            'F',        
           ],

}

df = pd.DataFrame(dados)

#muda os indices a partir de um vetor
df.index = [chr(i+65) for i in range(len(df))]
#printa toda a base
print(df)

#seleciona uma linha e coluna
#df.loc["A",:]
#print(df.loc["A",:])

#seleciona um intervalo de linhas e colunas
#df.loc["A",:]
#print(df.loc["A":"C",'Nome':'Idade'])

#seleciona linhas e colunas especificas
#df.loc[["A","E"],['Nome','Sobrenome','Sexo']]
#print(df.loc[["A","E"],['Nome','Sobrenome','Sexo']])

#funcionamento parecido com do loc, mas usa indice ao inves do nome
#print(df.iloc[0,0:3])

print('\n\n\n')
#media de idade
#print(df['Idade'].mean())

#variancia
#print(df['Idade'].var())

#desvio padrao
#print(df['Idade'].std())

#dados
print(df['Idade'].describe())

print('\n\n\n\n\n')

#tratamento dos dados em um intervalo
#dados

#print(df.iloc[[0,5],2].describe())

temp=df.loc[["A","E"],'Idade']
print(temp.describe())

