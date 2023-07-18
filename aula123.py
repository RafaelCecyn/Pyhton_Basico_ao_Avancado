# Escopo da classe e de métodos da classe

class Animal:
    # nome = 'Leão'
    
    def __init__(self,nome):
        self.nome = nome
        
        variavel = 'valor' # Variável somente desse método, não consigo acessar em outros métodos, pois não tem a palavra SELF
        print(variavel)
        
    def comendo(self,alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self,*args,**kwargs):
        return self.comendo(*args,**kwargs)
    
leao = Animal('Leão')
print(leao.nome)
print(leao.comendo('Maçã'))
print(leao.executar(alimento='Maçã'))
