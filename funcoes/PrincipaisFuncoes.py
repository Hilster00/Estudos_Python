#função sem retorno definido
def funcao0():
    ...
  
#função com retorno definido  
def funcao1():
    return 'Retorno'
 
#função com parametro   
def funcao2(variavel):
    return variavel

#função com parametro com valor padrão   
def funcao3(variavel='valor padrao'):
    return variavel
    
#função com mais de um parametro
def funcao4(variavel1,variavel2):
    return variavel1+variavel2

#função com apenas parametros posicionais e quantidade fixa
def funcao5(variavel1,variavel2,/):
    return variavel1+variavel2
   
#função com variavel posicional e variavel nomeada
def funcao6(variavel1,/,variavel2):
    return variavel1+variavel2
  
#funcao com quantidade de argumentos posicionais não fixas
def funcao7(*args):
    retorno=''
    for i in args:
        retorno+=f'{i}'
    return retorno
    
#funcao com apenas arumentos nomeados e quantidade fixa
def funcao8(*,variavel1,variavel2):
    return variavel1+variavel2
    
#função com apenas arumentos nomeados e quantidade não fixa    
def funcao9(**kwargs):
    retorno=''
    for i,j in kwargs.items():
        retorno+=f"{i}:{j}"
    return retorno
 
 
#combinações 

def funcao10(variavel1,/,variavel2,*,variavel3):
    return variavel1+variavel2+variavel3
    
def funcao11(*args,**kwargs):
    retorno=0
    for i in args:
        retorno+=i
    for key,i in kwargs.items():
        retorno+=i
    return retorno
    

#função anônima
funcao12=lambda i:i

if __name__=="__main__":
    print(funcao0())
    print(funcao1())
    print(funcao2(1))
    print(funcao3())
    print(funcao4(variavel2=2,variavel1=3))
    print(funcao5(4,5))
    print(funcao6(6,variavel2=7))
    print(funcao7(8,9,10))
    print(funcao8(variavel1=11,variavel2=12))
    print(funcao9(variavel1=13,variavel2=14))
    print(funcao10(15,variavel2=16,variavel3=17))
    print(funcao11(18,variavel2=19))
    print(funcao12(20))
