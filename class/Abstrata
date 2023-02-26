from abc import ABC
class Carta(ABC):
    def __init__(self,nome,texto):
        self.nome=nome
        self.texto=texto
    
    @property 
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self,nome):
        self.__nome=nome
    
    @property 
    def texto(self):
        return self.__texto
        
    @texto.setter
    def texto(self,texto):
        self.__texto=texto
    
class Monstro(Carta):
    def __init__(self,nome,nivel,texto,ataque,defesa,elemento,tipo,subtipo=None):
        Carta.__init__(self,nome,texto)
        self.__nivel=0
        self.nivel=nivel
        self.ataque=ataque
        self.defesa=defesa
        self.elemento=elemento
        self.tipo=tipo
        self.subtipo=subtipo
    
    #setter e geter nivel
    @property
    def nivel(self):
        return self.__nivel
        
    @nivel.setter
    def nivel(self,nivel):
        if 0 < nivel < 13:
            self.__nivel=nivel
            
    #setter e geter ataque
    @property 
    def ataque(self):
        return self.__ataque
        
    @ataque.setter
    def ataque(self,ataque):
        self.__ataque=ataque
     
    #setter e geter defesa   
    @property 
    def defesa(self):
        return self.__defesa
        
    @defesa.setter
    def defesa(self,defesa):
        self.__defesa=defesa
    
    #setter e geter elemento
    @property 
    def elemento(self):
        return self.__elemento
        
    @elemento.setter
    def elemento(self,elemento):
        self.__elemento=elemento
     
    #setter e geter tipo   
    @property 
    def tipo(self):
        return self.__tipo
        
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo=tipo
      
        
    #setter e geter subtipo
    @property 
    def subtipo(self):
        return self.__subtipo
        
    @subtipo.setter
    def subtipo(self,subtipo):
        self.__subtipo=subtipo
        
        
t=Monstro('nome',7,'texto',1500,0,'fogo','dragão')
