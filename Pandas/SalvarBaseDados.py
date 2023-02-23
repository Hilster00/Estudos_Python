import pandas as pd
import Pessoa_Random as pr

#recebe a estrutura de itens em pessoa_componetes
itens = pr.pessoa_componentes()

#cria um dict com chaves correspondendo a cada item que pessoa tem
pessoas={i:[] for i in itens}
del itens


#cria 100.000 pesssoas
for i in range(100_000):
    pessoa = pr.pessoa()

    #adiciona cada dado de uma pessoa a sua respectiva lista
    for chave,iten in pessoa.items():
        pessoas[chave].append(iten)

#converte o dict em um DataFrame
pessoas=pd.DataFrame(pessoas)

#salva os dados gerados em um arquivo
pessoas.to_csv('data.txt', sep='|', index=False)
