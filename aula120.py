# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de 
# classes.
# SELF REFERENCIA AO OBJETO QUE ESTÁ SENDO CRIADO
# string = 'Luiz' # str
# print(string.upper())
# print(isinstance(string,str))
class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    
    
p1 = Pessoa('Luiz','Otávio')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'
print(p1) # <__main__.Pessoa object at 0x0000023111E721D0>
print(p1.nome) # Luiz
print(p1.sobrenome) # Otávio

p2 = Pessoa('Maria','Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'
print(p2.nome) # Maria
print(p2.sobrenome) # Joana