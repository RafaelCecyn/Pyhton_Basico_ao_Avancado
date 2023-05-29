'''
args - Argumentos não nomeados É UMA TUPLA, empacota o que eu enviar a função em uma tupla
* - * args (empacotamento e desempacotamento)
'''

# Lembrete de desempacotamento
x, y, *resto = 1,2,3,4
print(x,y,resto)

def soma(*args):
    print(args)   # Empacotada (1,2,3,4,5,6)
    
soma(1,2,3,4,5,6)

def soma(*args):
    print(*args)   # Desempacotada 1 2 3 4 5 6
    
soma(1,2,3,4,5,6)


def soma(*args):
    soma = 0
    for i in args:
        soma += i
    print(soma)
        
soma(1,2,3,4,5,6)


def soma(*args):
    soma = 0
    for i in args:
        soma += i
    print(soma)
        
soma(1,2,3,4,5,6)

def soma(*args):
    soma = 0
    for i in args:
        soma += i
    return soma
        
soma_1_2_3_4_5_6 = soma(1,2,3,4,5,6)
print(soma_1_2_3_4_5_6)

print(sum((1,2,3,4,5,6))) # Sum

numeros = 1,2,3,4,5,6,7,78,10
outra_soma = soma(*numeros) # Desempacota pois já tenho uma tupla e o args empacota em outra tupla DESEMPACOTAR *args
print(outra_soma)