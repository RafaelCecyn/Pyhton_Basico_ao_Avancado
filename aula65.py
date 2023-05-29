'''
Introduções às funções (def) em Python
Funções são trechos de código usados para
replicar determinadas ações durante o código.
Elas podem receber valroes para parâmetros (argumentos)
e retorna um valor especpifico.
Por padrão, funções Python retornam None (nada).
'''

# def Print(a,b,c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# Print()

# def imprimir(a,b,c):
#     print(a,b,c)

# imprimir(1,2,3)

def saudacao(nome='Sem nome'):
    print(f'Olá {nome}')

saudacao('Stephany')
saudacao()