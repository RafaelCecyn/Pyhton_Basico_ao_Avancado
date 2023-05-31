# Manipulando chaves e valores em dicionários
pessoa = {}

#
#

chave = 'nome_completo'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'Maria'
del pessoa['sobrenome']

print(pessoa)

# Método get para dicionários tenta buscar a chave, se não encontrar volta NONE. Se encontrar retorna o valor da chave
print(pessoa.get('sobrenome')) # None

print(pessoa.get(chave)) # Maria

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa.get('sobrenome'))