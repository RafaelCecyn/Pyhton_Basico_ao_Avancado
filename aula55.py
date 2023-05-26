'''
Imprecisão de ponto flutuante
Double - precision floating point format IEEE-754
'''
import decimal

numero_1 = 0.7
numero_2 = 0.1
numero = numero_1 + numero_2
print(numero)
print(f'{numero:.1f}')
print(round(numero,2))

# Outra forma de resolver
numero_1 = decimal.Decimal(0.7)
numero_2 = decimal.Decimal(0.1)
numero = numero_1 + numero_2
print(numero)
print(f'{numero:.1f}')
print(round(numero,2))