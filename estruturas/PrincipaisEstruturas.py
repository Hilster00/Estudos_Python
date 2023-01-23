lista=list(range(10))
tupla=tuple(range(10))
dicionario=dict([[(i+1),f"{i+1}{chr(i+65)}"] for i in range(10)])
conjunto=set(range(10))

if __name__=="__main__":
    print(lista)
    print(tupla)
    print(dicionario)
    print(conjunto)
    
