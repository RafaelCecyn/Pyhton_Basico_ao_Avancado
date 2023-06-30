# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [], {} e set()
# Imutáveis (), "" 0 0.0 None False range(0,10)
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def falsy(valor):
    return 'falsy' if not valor else 'Truthy'

print('Teste', falsy('Teste'))
print('Lista', falsy(lista))
print('Dicionario', falsy(dicionario))
print('Conjunto', falsy(conjunto))
print('Tupla', falsy(tupla))
print('String', falsy(string))
print('Inteiro', falsy(inteiro))
print('Flutuante', falsy(flutuante))
print('Nada', falsy(nada))
print('Falso', falsy(falso))
print('Intervalo', falsy(intervalo))