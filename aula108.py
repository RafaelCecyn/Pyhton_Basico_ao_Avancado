"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def lista_soma(lista1,lista2):
    intervalo = min(len(lista1),len(lista2))
    
    return [
        (lista1[i]+lista2[i]) for i in range(intervalo)
    ]

print(lista_soma(lista_a,lista_b))


lista_soma = [x+y for x,y in zip(lista_a,lista_b)]
print(lista_soma)