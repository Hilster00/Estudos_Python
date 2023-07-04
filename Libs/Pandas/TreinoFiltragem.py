import Pessoa_Random
import pandas as pd

quantidade=100_000
#recebe todos os dados que pessoas tem
temp=Pessoa_Random.pessoa_componentes()

#adiciona espacos para guardar os dados
dados={}
for i in temp:
    dados[i]=[]
    
    
for i in range(quantidade):
    temp=Pessoa_Random.pessoa()
    for j,k in temp.items():
        dados[j].append(k)

d=pd.DataFrame(dados)
def q_sobrenome(linha):
    return linha['Sobrenome'].count(' ') == 1
def q_nome(linha):

    return linha['Nome'].count(' ') == 0

def filtro_idade(linha):
    return 25 >= linha['Idade'] >= 18
def filtro_altura(linha):
    return 1.65 >= linha['Altura'] >= 1.5
#filtro mulheres
mulheres=d[d['Sexo']=='F']

#filtro 2 sobrenomes
mulheres_2_sobrenomes=mulheres[mulheres.apply(q_sobrenome,axis=1)]

#filtro 1 nome
mulheres_1_nome=mulheres_2_sobrenomes[mulheres_2_sobrenomes.apply(q_nome,axis=1)]

#filtro adulta
mulheres_adultas=mulheres_1_nome[mulheres_1_nome.apply(filtro_idade,axis=1)]

mulheres_medianas=mulheres_adultas[mulheres_adultas.apply(filtro_altura,axis=1)]


print(mulheres_medianas)

print(f'Mulheres:{mulheres.shape}')
print(f'Mulheres 2 Sobrenomes:{mulheres_2_sobrenomes.shape}')
print(f'Mulheres 2 Nome:{mulheres_1_nome.shape}')
print(f'Mulheres Adultas:{mulheres_adultas.shape}')

print(f'Mulheres Medianas:{mulheres_medianas.shape}')

print(d[(d['Nome']=='Hilster') & (d['Idade']<=25)])
