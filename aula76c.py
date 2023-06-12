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

# d1 = {
#     'c1': 1,
#     'c2': 2,
# }

# d2 = d1 # Assim modifica o primeiro dicionário

# d2['c1'] = 1000

# print(d1)

# d1 = {
#     'c1': 1,
#     'c2': 2,
# }

# d2 = d1.copy() # Assim não modifica o primeiro dicionário

# d2['c1'] = 1000

# print(d1)

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2],
# }

# d2 = d1.copy() 

# d2['c1'] = 1000
# d2['l1'][1] = 999999

# print(d1) # Altera os valores mútaveis do primeiro dicionário {'c1': 1, 'c2': 2, 'l1': [0, 999999, 2]}
# print(d2) # {'c1': 1000, 'c2': 2, 'l1': [0, 999999, 2]}

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2],
}

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1) # Não altera os valores mútaveis do primeiro dicionário {'c1': 1, 'c2': 2, 'l1': [0,1, 2]}
print(d2) # {'c1': 1000, 'c2': 2, 'l1': [0, 999999, 2]}