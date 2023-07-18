# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2023
    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade 
    

dados = {'nome': 'Joâo', 'idade': 35}
p1 = Pessoa(**dados) # Mesma coisa que passar escrevendo, aqui por desempacotamento
# p1.nome = 'EITA'
# del p1.nome
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
print(p1.__dict__) # {'nome': 'Joâo', 'idade': 35}
print(vars(p1))  # {'nome': 'Joâo', 'idade': 35}