# Decoradores com parâmetros
# Função decoradora cria outras funções, são Factory functions

# def decoradora(func):
#     print('Decoradora 1')
    
#     def aninhada(*args,**kwargs):
#         print('Aninhada')
#         res = func(*args,**kwargs)
#         return res
#     return aninhada

# @decoradora()           # Executa a decoradora
# def soma(x,y):
#     return x + y

# dez_mais_cinco = soma(10,5)
# print(dez_mais_cinco)

def fabrica_de_funcoes(func):
    print('Decoradora 1')
    
    def aninhada(*args,**kwargs):
        print('Aninhada')
        res = func(*args,**kwargs)
        return res
    return aninhada

def fabrica_de_decoradores(a,b,c):
    return fabrica_de_funcoes

@fabrica_de_decoradores(1,2,3)             
def soma(x,y):
    return x + y

multiplica = fabrica_de_funcoes(lambda x,y: x*y)

dez_mais_cinco = soma(10,5)
dez_vezes_cinco = multiplica(10,5)
print(dez_mais_cinco)
print(dez_vezes_cinco)



def fabrica_de_decoradores(a=None,b=None,c=None): # Acesso aos parâmetros para acessar o decorador

    def fabrica_de_funcoes(func):
        print('Decoradora 1')
        
        def aninhada(*args,**kwargs):
            print('Parâmetros do decorador, ',a,b,c)
            print('Aninhada')
            res = func(*args,**kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1,2,3)             
def soma(x,y):
    return x + y

multiplica = fabrica_de_decoradores(1,2,3)(lambda x,y: x*y)

dez_mais_cinco = soma(10,5)
dez_vezes_cinco = multiplica(10,5)
print(dez_mais_cinco)
print(dez_vezes_cinco)