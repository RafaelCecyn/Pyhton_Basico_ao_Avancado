'''
Introdução ao try/except:
try -> tenta executar o código
except -> ocorreu erro ao tentar executar
'''

numero_str = input('Vou dobrar o nome digitado: ')

try:
    numero_float = float(numero_str)
    print('Float :', numero_float)
    print(f'O dobro de {numero_float} é {numero_float*2}')
except:
    print('Isso não é um número')