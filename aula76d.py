'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável coms as chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave específica (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
Um dicionário pode ter a mesma chave, mas vai armazenar o último valor
'''

p1 = {
    'nome':'Luiz',
    'sobrenome': 'Miranda',
}

# print(p1['nome'])
# print(p1.get('nome','Não existe'))

# nome = p1.pop('nome') # Luiz
# print(nome) # Luiz
# print(p1) # {'sobrenome': 'Miranda'}

# ultima_chave = p1.popitem() # {'sobrenome': 'Miranda'}
# print(ultima_chave) # {'sobrenome': 'Miranda'}
# print(p1) # {'nome': 'Luiz'}

# p1.update({
#     'nome': 'novo valor',
#     'idade': 30
# })
# p1.update(nome='novo valor', idade=30)
tupla = (('nome','novo valor'), ('idade',30)) 
lista = [['nome','novo valor'], ['idade',30]]
# p1.update(tupla) # {'nome': 'novo valor', 'sobrenome': 'Miranda', 'idade': 30}
p1.update(lista) # {'nome': 'novo valor', 'sobrenome': 'Miranda', 'idade': 30}
print(p1)