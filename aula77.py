# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

while True:
    chaves = list()
    valores = list()
    for pergunta in perguntas:
        for chave,valor in pergunta.items():
            chaves.append(chave)
            valores.append(valor)
            
    print(f'{chaves[0]}: {valores[0]}')
    print(f'{chaves[1]}:')
    print(f'0) {valores[1][0]}')
    print(f'1) {valores[1][1]}')
    print(f'2) {valores[1][2]}')
    print(f'3) {valores[1][3]}')
    escolha = input('Escolha uma opção: ')
    
    if escolha == '2':
        print('Você acertou')
    else:
        print('Você errou')
        
    print(f'{chaves[0]}: {valores[3]}')
    print(f'{chaves[1]}:')
    print(f'0) {valores[4][0]}')
    print(f'1) {valores[4][1]}')
    print(f'2) {valores[4][2]}')
    print(f'3) {valores[4][3]}')
    escolha = input('Escolha uma opção: ')
    
    if escolha == '0':
        print('Você acertou')
    else:
        print('Você errou')
    
    
    print(f'{chaves[0]}: {valores[6]}')
    print(f'{chaves[1]}:')
    print(f'0) {valores[7][0]}')
    print(f'1) {valores[7][1]}')
    print(f'2) {valores[7][2]}')
    print(f'3) {valores[7][3]}')
    escolha = input('Escolha uma opção: ')
    
    if escolha == '1':
        print('Você acertou')
    else:
        print('Você errou')
    
    
    
    break

# qtd_acertos = 0
# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao)
#     print()

#     escolha = input('Escolha uma opção: ')

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou 👍')
#     else:
#         print('Errou ❌')

#     print()


# print('Você acertou', qtd_acertos)
# print('de', len(perguntas), 'perguntas.')