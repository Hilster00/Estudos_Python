def funcao0():
    ...
    
def funcao1():
    return 'Retorno'
    
def funcao2(variavel):
    return variavel
    
def funcao3(variavel='valor padrao'):
    return variavel
    
def funcao4(variavel1,variavel2):
    return variavel1+variavel2
    
def funcao5(*args):
    retorno=''
    for i in args:
        retorno+=i
    return retorno
    
def funcao6(**kwargs):
    retorno=''
    for i,j in kwargs.itens():
        retorno+=f"{i}:{j}"
    return retorno
    
funcao7=lambda i:i
