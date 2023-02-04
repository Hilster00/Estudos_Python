class Contato:
    
    def __init__(self,email,telefone):
        self.__email=[email]
        self.__telefone=[telefone]

    
    #email 
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email):
        self.__email.append(email)
        
    def remover_email(self,indice):
        if 0 <= indice < len(self.__email):
            self.__email.pop(indice)
        else:
            raise ValueError(f"Indice {indice} não está no intervalo válido")
     
     
     
    #telefone       
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self,telefone):
        self.__telefone.append(telefone)
        
    def remover_telefone(self,indice):
        if 0 <= indice < len(self.__telefone):
            self.__telefone.pop(indice)
        else:
            raise ValueError(f"Indice {indice} não está no intervalo válido")
            

class Endereco:
    
    def __init__(self,numero,rua,bairro,cidade,estado,pais):
        self.numero=numero
        self.rua=rua
        self.bairro=bairro
        self.cidade=cidade
        self.estado=estado
        self.pais=pais
        
    #numero
    @property
    def numero(self):
        return self.__numero
        
    @numero.setter
    def numero(self,numero):
        self.__numero=numero
    
        
    #rua
    @property
    def rua(self):
        return self.__rua
        
    @rua.setter
    def rua(self,rua):
        self.__rua=rua
    
    
    
    #bairro
    @property
    def bairro(self):
        return self.__bairro
        
    @bairro.setter
    def bairro(self,bairro):
        self.__bairro=bairro
    
    
    
    #cidade
    @property
    def cidade(self):
        return self.__cidade
        
    @cidade.setter
    def cidade(self,cidade):
        self.__cidade=cidade
    
    
    
    #estado
    @property
    def estado(self):
        return self.__estado
        
    @estado.setter
    def estado(self,estado):
        self.__estado=estado
    
    
    
    #pais
    @property
    def pais(self):
        return self.__pais
        
    @pais.setter
    def pais(self,pais):
        self.__pais=pais
        
    def __str__(self):
        r=f'''Rua:{self.rua}, Numero:{self.numero}, Bairro:{self.bairro}, Cidade:{self.cidade}, Estado:{self.estado}, Pais:{self.pais}'''
        return r
        
        
        
class Pessoa:
    
    def __init__(self,nome,contato,endereco):
        self.__nome=None
        self.nome=nome
        self.contato=contato
        self.__endereco=[]
        self.endereco=endereco
        self.t=[1,2,3]
        self.v=0
    
    #nome 
    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self,nome):
        if self.__nome==None:
            self.__nome=nome
     
    
    #contato       
    @property
    def contato(self):
        return self.__contato
        
    @contato.setter
    def contato(self,contato):
        self.__contato=contato
    


    #endereco
    @property
    def endereco(self):
        return self.__endereco
        
    @endereco.setter
    def endereco(self,endereco):
        self.__endereco.append(endereco)
        
    def remover_endereco(self,indice):
        if 0 <= indicie < len(self.__endereco):
            self.__endereco.pop(indicie)
        else:
            raise ValueError(f"Indice {indicie} não está no intervalo válido")
    
    
    def __str__(self):
        retorno=f'Nome:{self.nome}\n\nE-Mails:\n'
        for i in self.contato.email:
            retorno+=f'{i}\n'
        retorno+='\nTelefones:\n'
        for i in self.contato.telefone:
            retorno+=f'{i}\n'
        retorno+='\nEnderecos:\n'
        
        for i in self.endereco:
            retorno+=f'{i}\n'
        return retorno
        
        

class sala:
    
    def __init__(self,turma,alunos=[]):
        self.__turma=turma
        self.__alunos=alunos
        self.__p=0
        self.__q=len(alunos)
        
    def adicionar_aluno(self,aluno):
        self.__alunos.append(aluno)
        
        
    
   
    
    
            
    @property
    def turma(self):
        return self.__turma
        
    @property
    def alunos(self):
        return self.__alunos
    
    
        
contato=Contato('fyjhchilster.santos@gmail.com','64999786370')
endereco=Endereco('2001','rua','Bairro','Jataí','GO','Brasil')
hilster=Pessoa('Hilster Barbosa Santos',contato,endereco)
print("_"*50,'Teste 1',"_"*50)
print(hilster)
hilster.contato.email='hilsterb.santos@gmail.com'
print("_"*50,'Teste 2',"_"*50)
print(hilster)
hilster.contato.telefone='40028922'
print("_"*50,'Teste 3',"_"*50)
print(hilster)
hilster.contato.remover_email(0)
print("_"*50,'Teste 4',"_"*50)
print(hilster)
hilster.contato.remover_telefone(1)
print("_"*50,'Teste 5',"_"*50)
#print(hilster)
turma=sala('Ciência da Computação')
turma.adicionar_aluno(hilster)
print(turma.alunos)
print(hilster)

for i in turma:
    print(i)
    
#print(next(turma))
