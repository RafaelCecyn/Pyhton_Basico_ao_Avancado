# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def multiplica(*args):
    total = 1
    for i in args:
        total *= i
    return total
        
variavel_multiplica = multiplica(1,2,3,4,5)
print(variavel_multiplica)


def fala(numero):
    if numero % 2 == 0:
        return 'par'
    return 'ímpar'

numero_escolhido = fala(12)
numero_escolhido_2 = fala(11)
print(numero_escolhido,numero_escolhido_2)