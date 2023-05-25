# Operador in e not in
# Strings são iteráveis
#  0  1  2  3  4  5
#  O  T  Á  V  I  O
# -6 -5 -4 -3 -2 -1

nome = 'Otávio'

print('á' in nome)
print('z' in nome)
print('vio' not in nome)
print('zero' not in nome)

nome_digitado = input('Digite um nome: ')
encontrado = input('Digite o que quer encontrar: ')

if encontrado in nome_digitado:
    print(f'{encontrado} está em {nome_digitado}')
else:
    print(f'{encontrado} não está em {nome_digitado}')