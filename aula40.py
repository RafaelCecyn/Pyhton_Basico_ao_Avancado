# Calculadora

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite um número: ')
    operador = input('Digite uma operação (+-*/): ')

    operadores_permitidos = '+-*/'

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    
    numeros_validos = None

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
        print('Estamos realizado a sua conta: ')
        if operador == '+':
            soma = numero_1_float + numero_2_float
            print(f'{numero_1_float} + {numero_2_float} =',soma)
        elif operador == '-':
            subtracao = numero_1_float - numero_2_float
            print(f'{numero_1_float} - {numero_2_float} =',subtracao)
        elif operador == '*':
            multiplicacao = numero_1_float * numero_2_float
            print(f'{numero_1_float} * {numero_2_float} =',multiplicacao)
        elif operador == '/' and numero_2_float != 0:
            divisao = numero_1_float / numero_2_float
            print(f'{numero_1_float} / {numero_2_float} =',divisao)

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou mais números estão errados: ') 

    sair = input('Você quer [s]air: ').lower().startswith('s')
    # starswidth return bool

    if sair is True:
        break