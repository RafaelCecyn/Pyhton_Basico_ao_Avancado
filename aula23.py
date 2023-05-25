# Operador lógico 'not'
# Usado para inverter expressões
# not True = False
# not False = True

senha = input("Digite uma senha: ")

if not senha:
    print('Não digitou uma senha')
else:
    print('Digitou uma senha')