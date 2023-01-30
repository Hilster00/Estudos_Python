class vetor:
    def __init__(self, vetor=[]):
        self.__valores = vetor
        self.__tamanho = len(vetor)
        self.__posicao = 0
     
    #permite iteração por for   
    def __iter__(self):
        return iter(self.__valores)
        
    
    #permite iteração por next    
    '''def __next__(self):
        if self.__posicao == self.__tamanho:
            self.__posicao=0
            raise StopIteration
        r = self.__valores[self.__posicao]
        self.__posicao += 1
        return r'''
    def __str__(self):
        r='Vetor do Hilster : {'
        for i in self.__valores:
            r+=f'{i},'
        r+='}'
        return r
 
     
vet=vetor(list(range(10)))

#este deve rodar
for i in vet:
    print(i)

#print(next(vet))

