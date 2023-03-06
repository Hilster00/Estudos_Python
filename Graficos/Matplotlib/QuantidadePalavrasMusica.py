import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def filtrar(letra):
    letra=letra.lower()
    letra=letra.replace(","," ")
    letra=letra.replace("\n"," ")
    letra=letra.split(" ")
    letra.sort()
    return [i for i in letra if i != ""]

def contagem(letra):
    #conta quantidade de vezes que a palavra aparece
    temp={}
    anterior=None
    for i in letra:
        if i != anterior:
            temp[i]=1
            anterior=i
        else:
            temp[i]+=1
    return temp


#classe para criar uma base de dados
class base_dados:
    """
    Esta base de dados depois de criada, sempre permite que adicionem mais dados a ela,
    ela adiciona dados como se fosse uma nova linha, para isso ele permite apenas recebimento de novos dados
    do tipo dict, caso esse dict recebido tenha uma chave não cadastrada nos dados, ele cria uma nova e atribui None
    aos valores para as linhas anteriores.
    """
    def __init__(self,dados={}):
        #cria base de dados vazia e pede para o setter receber os dados
        self.__dados={}
        self.__quantidade_linhas=0

        """
        CORREçÃO DE BUG
        Como ele criava a base de dados usando o proprio setter, ele adicionava um a quantidade de linhas,
        independente de ter ou não colocado dados
        """
        if dados != {}:
            self.dados=dados
        
    def __iter__(self):
        return iter(self.dados)
    
    @property
    def linhas(self):
        return self.__quantidade_linhas
    
    @property
    def dados(self):
        return self.__dados
    
    @dados.setter
    def dados(self,dados={}):
        #tratamento de erro
        if type(dados) == dict:
            
            for chave,valor in dados.items():
                #verifica se a chave já está cadastrada
                if self.__dados.get(chave) == None:
                    #cria a chave e atribui None para as linhas de dados anteriores
                    self.__dados[chave]=[None for i in range(self.__quantidade_linhas)]
                self.__dados[chave].append(valor)

                
            self.__quantidade_linhas+=1

            #atribui None para as chaves que os dados carregado não possui
            for chave,valor in self.__dados.items():
                if len(valor) != self.__quantidade_linhas:
                    self.__dados[chave].append(None)
        else:
            raise ValueError(f"{dados} Não pertence ao tipo dict")

    
musica1="""
These trials make us who we are, who we are, we are
We're motivated by the scars that we're made of
These trials make us who we are, who we are, we are
We take our places in the dark
And turn our hearts to the stars
Hear me from the bottom
Forged in regret, I'm the silversmith
Doomsday, you had it coming
Marching the streets with an iron fist
Obey no more in silence
The steel in our hearts will be monuments
Today, they'll hear the violence
We'll rise from the dark like Lazarus
These trials make us who we are, who we are, we are
We're motivated by the scars that we're made of
These trials make us who we are, who we are, we are
We take our places in the dark
And turn our hearts to the stars
The ending won't be forgotten
It's written in the stars and the hieroglyphs
Sending the lionhearted
The stones break bones, but we're venomous
These trials make us who we are, who we are, we are
We're motivated by the scars that we're made of
These trials make us who we are, who we are, we are
We take our places in the dark
And turn our hearts to the stars
Calling, calling, we've come out to play
Show me, show me a new way
Slowly, slowly, they've led you astray
Away we go now into the fray
These trials make us who we are, who we are, we are
We're motivated by the scars that we're made of
These trials make us who we are, who we are, we are
We take our places in the dark
And turn our hearts to the stars
Step forward for synchronization
Please select an item to be printed
You do not have access to that item
Do you wish to proceed?
You have three thousands and twenty seven credits, please select
You do not have access to that item
Do you?
You do not have access to that item
Do you
Please exit the platform
Please exit the platform
Please ex
"""

musica2="""
I feel it everyday, it's all the same
It brings me down, but I'm the one to blame
I've tried everything to get away
So here I go again
Chasing you down again
Why do I do this?
Over and over, over and over
I fall for you
Over and over, over and over
I try not to
It feels like everyday stays the same
It's dragging me down, and I can't pull away
So here I go again
Chasing you down again
Why do I do this?
Over and over, over and over
I fall for you
Over and over, over and over
I try not to
Over and over, over and over
You make me fall for you
Over and over, over and over
You don't even try
So many thoughts that I can't get out of my head
I try to live without you
Every time I do, I feel dead
I know what's best for me
But I want you instead
I'll keep on wasting all my time
Over and over, over and over
I fall for you
Over and over, over and over
I try not to
Over and over, over and over
You make me fall for you
Over and over, over and over
You don't even try to
"""

musica3="""
Show me your insides
Show me your secrets
Show me what you desire
I can fake it
Show what you wanted
So I can be it
And if I bend just right
I can make it
I didn't want you
I wanna watch you change
From a butterfly and into chains
Lay your heart into my perfect machine
I will show you what you wanted to see
Just a mirror 'til I get what I need
The reverie was not of me
You never saw nothing
Never saw nothing
I'm just a liar
Without deceiving
I'm just a broken clown
Make believing
I should've let you know
You should've ran for cover
I'm just a parlor trick
A two-bit counterfeit
Lay your heart into my perfect machine
I will use it to protect you from me
I will never let you see what's beneath
So good for you and good for me
We told ourselves we're right where we ought to be
Even you know
Even you know
This was all for nothing
Just a sad show
Just an ego
I suppose though
As far as I know
We were both pretending
I suppose so
But what do I know?
Even you know
Even you know
This was all for nothing
Just a sad show
Just an ego
I suppose though
As far as I know
We were both pretending
I suppose so
But what do I know?
Lay your heart into my perfect machine
I will show you what you wanted to see
Just a mirror 'til I get what I need
The reverie was not of me
You never saw nothing
Never saw nothing
Lay your heart into my perfect machine
I will use it to protect you from me
I will never let you see what's beneath
So good for you and good for me
We told ourselves we're where right we ought to be
"Unity
Through allegiance
A strong party
Brings happiness to the people
Hard work makes a powerful nation
Contraband thought will result in audit and subjugation"
"Next destination
New East facility 23
Next destination
New East facility 23"
"""

#limpagem e filtragem de dados
musica1=filtrar(musica1)
musica1=contagem(musica1)

musica2=filtrar(musica2)
musica2=contagem(musica2)

musica3=filtrar(musica3)
musica3=contagem(musica3)

#adicionando a base de dados        
dados=base_dados()
dados.dados=musica1
dados.dados=musica2
dados.dados=musica3
dados=pd.DataFrame(dados.dados)

#lista de palavras
palavras=list(dados.columns)

#filtrando dados de cada linha
musica1=dados.loc[0]
quantidade_musica1=np.array([0 if pd.isnull(i) else i for i in musica1])
#pd.isnull verifica se i é nulo pois o vetor desta coluna possui valores numericos, e somente essa função verifica para valores do pandas

musica2=dados.loc[1]
quantidade_musica2=np.array([0 if pd.isnull(i) else i for i in musica2])

musica3=dados.loc[2]
quantidade_musica3=np.array([0 if pd.isnull(i) else i for i in musica3])

#adiciona os espacamentos do eixo x
espacamento=np.array([i*10 for i in range(len(quantidade_musica1))])


#plot da proproção das palavras
plt.plot(espacamento,quantidade_musica1,label='Trials')
plt.plot(espacamento,quantidade_musica2,label='Over and Over')
plt.plot(espacamento,quantidade_musica3,label='Perfect Machine')
plt.legend()
"""
não curti muito
"""
plt.show()

#plot grafico de barras de intervalo de 10 palavras
for i in range(10):
    plt.bar(palavras[i*10:(i+1)*10], quantidade_musica1[i*10:(i+1)*10],label='Trials')
    plt.bar(palavras[i*10:(i+1)*10], quantidade_musica2[i*10:(i+1)*10],label='Over and Over')
    plt.bar(palavras[i*10:(i+1)*10], quantidade_musica3[i*10:(i+1)*10],label='Perfect Machine')
    plt.legend()
    plt.savefig(f'grafico barras de palavras {i+1}.png')
    plt.show()
    plt.clf()
