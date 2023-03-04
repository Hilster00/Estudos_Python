#lista de valores em uma string
lista="01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"

intervalo=10

#ListComprehension para agrupar a string de um intervalo especifico
#lista comeca em i e vai até i+10, agrupando de 10 em 10, como i cresce de 10 em 10, 
#sempre será obtido um intervalo de 10 digitos( 0-9, 10-19, ... )
lista=[lista[i:intervalo+i] for i in range(0,len(lista),intervalo)]

retorno = ".".join(lista)
print(lista)
print(retorno)
