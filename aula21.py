# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliado naquela valor
# São considerados falsy
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor
entrada = input('[E]ntrar ou [S]air ')
senha_digitada = input('Digite sua senha: ')

senha_permitida = '123456'

if entrada == "E" and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
print(True and False and True)
print(True and 0 and True)


