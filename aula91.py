# Introdução às Generators functions em Python
# generator = (n for n in range(10000))


# def generator(n=0):
#     yield 1 # pausar
#     print('Continuando... ')
#     yield 2 # pausar
#     print('Mais uma')
#     yield 3 # pausar
#     print('Vou terminar')
    
    
# gen = generator(n=0)
# for n in gen:
#     print(n)    
    
    
def generator(n=0,maximum=10):
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return
        
gen = generator()
for n in gen:
    print(n) 