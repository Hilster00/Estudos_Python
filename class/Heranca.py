from Pessoa import Pessoa,Contato,Endereco

class Aluno(Pessoa):
    
    def __init__(self,nome,contato,endereco,matricula):
        Pessoa.__init__(self,nome,contato,endereco)
        self.__matricula=matricula
        
        self.i=0 
        self.v=[1,2,3]
        
    @property
    def matricula(self):
        return self.__matricula
        
    
    def __str__(self):
        r=Pessoa.__str__(self)
        
        r+=f'\nMatricula:{self.__matricula}'
        return r
        
class Turma:
    
    def __init__(self,nome,sigla):
        self.__nome=nome
        self.__sigla=sigla
        self.__alunos=[]
        self.__quantidade_alunos=0
        self.__i=0
        
    @property 
    def nome(self):
        return self.__nome
        
    @property 
    def sigla(self):
        return self.__sigla
    def append(self,aluno):
        self.__alunos.append(aluno)
        self.__quantidade_alunos+=1
        self.__i=0
        
    def remover(self,i):
        self.__alunos.pop(i)
        self.__quantidade_alunos-=1
        self.__i=0
        
    def __len__(self):
        
        return self.__quantidade_alunos
        
    def __getitem__(self,i):
        if 0 <= i < self.__quantidade_alunos:
            return self.__alunos[i]
        return None
      
    def __iter__(self):
        return self   
        
    def __next__(self):
        
        if self._i < self._quantidade_alunos:
            r = self._alunos[self._i]
            self.__i+=1
            return r
        else:
            self.__i=0
            raise StopIteration


if __name__ == '__main__':
    apa=Turma('Apa','apa')
    
    contato=Contato('hilsterb.santos@gmail.com','64999786370')
    endereco=Endereco('2001','rua','Bairro','Jataí','GO','Brasil')
    aluno=Aluno('Hilster Barbosa Santos',contato,endereco,2020102030)
    apa.append(aluno)
    
    contato=Contato('carloshenrique.50anos@gmail.com','64999999999')
    endereco=Endereco('1972','rua','Bairro','Jataí','GO','Brasil')
    carlos=Aluno('Carlos Henrique Carvalho Ferreira',contato,endereco,2020102031)
    apa.append(aluno)
    
    contato=Contato('carlosaless1512@gmail.com','64998765432')
    endereco=Endereco('2001','rua','Bairro','Jataí','GO','Brasil')
    aluno=Aluno('Carlos Alessandro Fernandes de Oliveira',contato,endereco,2020102032)
    apa.append(aluno)
    
    
    for i in apa:
        print(i)

