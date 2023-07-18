# Atributos de classe
class Pessoa:
    ano_atual = 2023 # Atributo da classe
    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100 # Cuidado pois vai pegar aqui primeiro e não do atributo da classe
        
    def ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade # Forma mais segura de fazer
        return self.ano_atual - self.idade # Perigoso pois pega dos métodos irmãos e não do atributo da classe
    
    
p1 = Pessoa('Maria',26)
print(Pessoa.ano_atual) # 2023
# Pessoa.ano_atual = 1 # Assim é perigoso pois altero o atributo da classe
print(p1.ano_de_nascimento())
print(Pessoa.ano_de_nascimento(p1))