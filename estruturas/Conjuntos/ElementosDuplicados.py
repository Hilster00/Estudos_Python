lista=[
    [1,2,3,4,5,6,7,8,9,3],
    [7,2,3,2,3,5,2,7,9,2],
    [9,9,3,7,0,3,2,1,0,0],
    [3,1,5,7,4,6,3,0,1,7],
    [1,2,3,4,5,6,7,8,9,0],
    [0,1,2,3,4,5,6,7,8,9],
    [1,1,4,2,3,7,5,6,4,3],
    [8,4,6,9,7,1,3,0,4,6],
    [9,8,7,6,5,4,3,2,1,0],
    [5,4,6,7,1,0,3,9,2,8]
]

def retornarDuplicado1(lista):
    temp=set(lista)
    if len(temp) == len(lista):
        return -1
    temp=[]
    for elemento in lista:
        if elemento not in temp:
            temp.append(elemento)
        else:
            return elemento
        
 def retornarDuplicado2(lista):
    temp=[]
    
    for elemento in lista:
        if elemento in temp:
            return elemento
        temp.append(elemento)
    return -1

def retornarDuplicado3(lista):
    temp=set()
    for elemento in lista:
        if elemento in temp:
           return elemento
        temp.add(elemento)
    return -1 


print("Elementos repetidos")
for lista_local in lista:
    print(f"{lista_local} Primeiro elemento repetido:{retornarDuplicado1(lista_local)}")
    print(f"{lista_local} Primeiro elemento repetido:{retornarDuplicado2(lista_local)}")
    print(f"{lista_local} Primeiro elemento repetido:{retornarDuplicado3(lista_local)}")
    
