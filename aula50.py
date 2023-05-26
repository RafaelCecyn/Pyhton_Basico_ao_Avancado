'''
Exercício - Exiba os índices
for in com listas
'''

# lista = ['Maria','Anna','Flávia']
# i = 0
# for nome in lista:
#     print(nome,i)
#     i+=1
    
# Outra forma


lista = ['Maria','Anna','Flávia']
indice = range(len(lista))
for i in indice:
    print(i, lista[i],type(lista[i]))