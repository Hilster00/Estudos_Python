import random 

#lista
lista=[chr(i) for i in range(ord("A"),ord("Z")+1)]

#semente que gera os números aleatórios
#random.seed(10)

#número aleatório de 1 a 10
aleatorio1=random.randint(1,10)
print(aleatorio1)

#número aleatório par de 1 a 10  
aleatorio2=random.randrange(2,10,2)
print(aleatorio2)

#número aleatório flutuante entre 1 e 10
aleatorio3=random.uniform(1,10)
print(aleatorio3)

#lista não embaralhada
aleatorio4=lista.copy()
print(aleatorio4[0:11])

#embaralha lista
random.shuffle(aleatorio4)
print(aleatorio4[0:11])


#cria uma nova lista, embaralha e corta os k primeiros elementos
#por isso os valores não repetem
aleatorio6=random.sample(lista,k=11)
print(aleatorio6)


#sorteia um valor da lista
aleatorio5=random.choice(lista)
print(aleatorio5)

#sorteia valores k vezes da lista e cria um vetor
#por isso os valores podem repetir
aleatorio7=random.choices(lista,k=11)
print(aleatorio7)

