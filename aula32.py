"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um numero inteiro: ')


try: 
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
except:
    print('Digite um número inteiro')
    

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite uma hora em números inteiros: ')


try:
    hora_int = int(hora)
    if hora:
        if hora_int <= 11:
            print(f'Bom dia {hora}')
        elif hora_int <= 17:
            print(f'Boa tarde {hora}')
        elif hora_int <= 23:
            print(f'Boa noite {hora}')
except:
    print('Digite uma hora válida')
    

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu nome: ')


if nome:
    if len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) <=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite alguma coisa')