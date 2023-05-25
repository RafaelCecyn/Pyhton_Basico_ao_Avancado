'''
Iterando sobre strings com while
'''

nome = 'Luiz Otávio' # Iteráveis

tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

nova_string = ''
condicao = 0

while condicao < tamanho_nome:
    # print(f'{nome[condicao]}')
    nova_string += f'*{nome[condicao]}'
    condicao+=1
    
print(nova_string)