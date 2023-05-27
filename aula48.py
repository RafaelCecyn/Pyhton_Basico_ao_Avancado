'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
'''

#        01234
#       -54321
string = 'ABCDE' # 5 Caracteres (len)
# lista = []
# print(bool(lista)) # falsy
# print(lista,type(lista))

lista = [123, True, 'Luiz Otávio', 1.2, []]
lista[-3] = 'Maria'
# print(lista[2].upper(),type(lista[2]))


'''
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar Ler alterar e apagar = lista[i] (Crud)


'''

lista_2 = [10,20,30,40]
lista_2[2] = 300 # Altera o valor do 30
print(lista_2)
del lista_2[2] # Deleta o 300 e o 40 vira o 3 posição
print(lista_2)
lista_2.append(50) # Insere um número ao final
lista_2.append(60)
lista_2.append(70)
print(lista_2)
lista_2.pop() # Remove do final se não especificado índice
print(lista_2)
lista_2.pop(1) # Remove do indice passado
print(lista_2)


'''
Métodos úteis:
append -> adiciona um item no final da lista
insert -> adiciona um item em qualquer posição da lista
pop - Remove no final ou em qualquer indice escolhido
del - apaga um índice
extend - estende a lista
+ - concatena a lista
'''

lista_3 = [10,20,30,40]
lista_3.append(50)
lista_3.insert(0,100)
del lista_3[3]
print(lista_3)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
lista_d = lista_a.extend(lista_b) # Retorna None na lista_d
print(lista_c)
print(lista_a) # igual a lista C


'''
Cuidado com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor da memória (mutável)
'''

lista_ab = ['João','Maria']
lista_ac = lista_ab
lista_ab[0] = 'Luiz' # Altera tanto na lista ab como na lista ac
print(lista_ac)

lista_e = ['Rafael', 'Stephany']
lista_f = lista_e.copy() # não altera o array original, preserva
lista_f[0] = 'Anna'
print(lista_e,lista_f)