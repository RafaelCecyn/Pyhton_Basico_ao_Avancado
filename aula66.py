'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x,y,z):
    print(f'{x=} y={y} {z=}',' | ', 'x + y + z = ', x + y + z)

soma(1,2,3) # Argumentos não nomeados
soma(1,y=2,z=3) # Argumentos nomeados, A PARTIR DO Y TODOS OS ARGUMENTOS PRECISAM SER NOMEADOS