'''
enumerate - enumera iteráveis (índices)
'''

lista = ['João','Maria','Anna']
lista.append('Rafael')

for item in enumerate(lista):
    indice,nome = item
    print(indice,nome)
    
# Outra forma

for indice, item in enumerate(lista):
    print(indice,item)