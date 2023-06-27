# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a

print(a,b) # 2,1

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}
a, b = pessoa # a -> nome, b -> sobrenome
a, b = pessoa.values() # a -> Aline, b -> Souza
a, b = pessoa.items() # a -> ('nome', 'Aline'), b -> ('sobrenome', 'Souza')
(a1,a2), (b1,b2) = pessoa.items()
print(a1,a2) # a1 -> nome, a2 -> Aline
print(b1,b2) # b1 -> sobrenome, b2 -> Souza
print(a,b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa,**dados_pessoa} # ** junta os dicionários
print(pessoa_completa) # {'nome': 'Aline', 'sobrenome': 'Souza', 'idade': 16, 'altura': 1.6}

# def mostro_argumetos_nomeados(*args,**kwargs):
#     print(kwargs) # {'nome': 'Joana', 'qlq': 123}


def mostro_argumetos_nomeados(*args,**kwargs):
    for chave, valor in kwargs.items():
        print(chave,valor) # nome Joana
                           # qlq 123
    
mostro_argumetos_nomeados(nome='Joana',qlq=123) # Empacotar
mostro_argumetos_nomeados(**pessoa_completa) # Desempacotar # nome Aline
                                                            # sobrenome Souza
                                                            # idade 16
                                                            # altura 1.6