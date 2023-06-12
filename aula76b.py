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

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 28
# }

# # print(len(pessoa)) # retorna o número de chaves
# # print(pessoa.keys()) # retorna nome, sobrenome
# print(pessoa.values()) # retorna Luiz Otavio Miranda
# print(pessoa.items()) # retorna nome Luiz Otavio sobrenome Miranda

# for chave in pessoa.keys():
#     print(chave)
    
# for valor in pessoa.values():
#     print(valor)
    
    
# for chave,valor in pessoa.items():
#     print(chave,valor)
    
    
# pessoa.setdefault('idade',None) # Se não tiver a chave retorna None
# print(pessoa['idade'])

'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave específica (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
'''

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
}

print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
print(list(pessoa.items()))

# for chave in pessoa.keys():
#     print(chave)
    
# for valor in pessoa.values():
#     print(valor)
    
    
for valor in pessoa.items():
    print(valor)
    
print(pessoa.setdefault('idade',0))
