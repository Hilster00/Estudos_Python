import Pessoa_Random
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

quantidade=100
#recebe todos os dados que pessoas tem
temp=Pessoa_Random.pessoa_componentes()

#adiciona espacos para guardar os dados
dados={}
for i in temp:
    dados[i]=[]

#adiciona as pessoas aos dados   
for i in range(quantidade):

    #pessoa gerada aleatoriamente
    temp=Pessoa_Random.pessoa()
    for j,k in temp.items():
        #dado cadastrado em seu respectivo local, na base de dados
        dados[j].append(k)

d=pd.DataFrame(dados)

#filtra as alturas e idades
temp=d.loc[:,['Idade','Altura']]

#converte cada linha para um dicionário
temp=temp.to_dict(orient='records')

#ordena a lista pelas chaves de cada dicionário interno
temp=sorted(temp,key=lambda i:i['Idade'])

#converte a lista de dicionários em uma lista com apenas o valor de uma chave especifíca
idades=np.array([i['Idade'] for i in temp])
alturas=np.array([i['Altura'] for i in temp])


plt.ylabel('Altura')
plt.xlabel('Idade')
plt.title('Distribuição de Alturas Por idade')

#plota as alturas de acordo com as 100 alturas cadastradas
plt.plot(idades, alturas)

plt.savefig('grafico.png')

plt.show()

