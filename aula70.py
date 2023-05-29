'''
Retorno dos valores da função (return) -> Padrão retorna none
Return interrompe o que vem abaixo
'''

def soma(x , y):
    if x > 10:
        return 10,20
    return x + y


soma1 = soma(2,2)
soma2 = soma(3,3)
print(soma1 + soma2)
soma3 = soma(50,100)
print(soma3)