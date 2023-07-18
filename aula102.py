# Variáveis livres + nonlocal (locals,globals)
# print(globals()) # mostra as variáveis globais

# def fora(x):
#     a = x # Variável livre pois não está definida dentro do escopo da variável dentro
#     def dentro():
#         print(locals()) # mostra as variáveis locais
#         print(dentro.__code__.co_freevars)
#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())


def concatenar(string_inicial):
     valor_final = string_inicial
     
     def interna(valor_a_concaternar):
        nonlocal valor_final # busca no escopo acima
        valor_final += valor_a_concaternar # erro no valor_final, pois não é desse escopo, só podemos ler e não alterar -> Mas definimos como non-local temos acesso
        return valor_final # variável livre
     return interna
 
 
c = concatenar('a')
print(c('b')) # Passa o parâmetro para a função interna
print(c('c')) # Passa o parâmetro para a função interna
print(c('d')) # Passa o parâmetro para a função interna