'''
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (maiúsculo e minúsculo)
'''

nome = 'Luiz'
preco = 100.23332
variavel = '%s, o preco é R$%.2f' % (nome,preco)
print(variavel)
print('O hexadecimal de %i é %x' % (15,15) )