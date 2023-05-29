"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '746.824.890-70'.replace('.','').replace('-','')

# sum = 0
# for i, m in enumerate(range(10,1,-1)):
#     sum += int(cpf[i]) * m

# print(sum)


# num1,num2,num3,num4,num5,num6,num7,num8,num9,*_ = cpf
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)
# num4 = int(num4)
# num5 = int(num5)
# num6 = int(num6)
# num7 = int(num7)
# num8 = int(num8)
# num9 = int(num9)
# lista = [num1,num2,num3,num4,num5,num6,num7,num8,num9]

lista = list()
for i in cpf[:-2]:
    lista.append(int(i))
lista.reverse()
print(lista)

soma = 0
for indice,valor in enumerate(lista,2):
    soma += indice*valor

resultado = soma * 10
resto = resultado % 11
primeiro_digito = resto if resto <= 9 else 0
print(primeiro_digito)

lista = list()
for i in cpf[:-1]:
    lista.append(int(i))
lista.reverse()
print(lista)

soma = 0
for indice,valor in enumerate(lista,2):
    soma += indice*valor

resultado = soma * 10
resto = resultado % 11
segundo_digito = resto if resto <= 9 else 0
print(segundo_digito)


"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
# import re
# import sys

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
# entrada = input('CPF [746.824.890-70]: ')
# cpf_enviado_usuario = re.sub(
#     r'[^0-9]',
#     '',
#     entrada
# )

# entrada_e_sequencial = entrada == entrada[0] * len(entrada)

# if entrada_e_sequencial:
#     print('Você enviou dados sequenciais.')
#     sys.exit()

# nove_digitos = cpf_enviado_usuario[:9]
# contador_regressivo_1 = 10

# resultado_digito_1 = 0
# for digito in nove_digitos:
#     resultado_digito_1 += int(digito) * contador_regressivo_1
#     contador_regressivo_1 -= 1
# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0

# dez_digitos = nove_digitos + str(digito_1)
# contador_regressivo_2 = 11

# resultado_digito_2 = 0
# for digito in dez_digitos:
#     resultado_digito_2 += int(digito) * contador_regressivo_2
#     contador_regressivo_2 -= 1
# digito_2 = (resultado_digito_2 * 10) % 11
# digito_2 = digito_2 if digito_2 <= 9 else 0

# cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
#     print(f'{cpf_enviado_usuario} é válido')
# else:
#     print('CPF inválido')

