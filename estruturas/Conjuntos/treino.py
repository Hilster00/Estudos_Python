lista1 =list(range(1,5))
lista2 =list(range(4,10))
lista1,lista2  = set(lista1),set(lista2)

uniao = list(lista1 | lista2)
intecessao = list(lista1 & lista2)
diferenca1 = list(lista1 - lista2)
diferenca2 = list(lista2 - lista1)
diferenca = list(lista1 ^ lista2)

print(uniao)
print(intecessao)
print(diferenca1)
print(diferenca2)
print(diferenca)
