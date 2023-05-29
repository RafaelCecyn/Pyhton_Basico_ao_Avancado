'''
Valores padrão para parâmetros
AO definir uma função, os parâmetros podem 
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: eidtar o seu código
'''

def soma(x,y,z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x+y+z)
    else:
        print(x + y)
    
    
soma(2,4)
soma(100,40)
soma(100,40,0)
soma(z=0,y=40,x=100)