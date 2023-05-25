'''
Repetições
while (enquanto)
Executa uma ação enquanto a condição é VERDADEIRA
Loop infinito -> Quando um código não tem fim
'''

condicao = True

while condicao:
    nome = input('Digite o seu nome: ')
    print(f'O seu nome é {nome}')
    
    if nome == "sair":
        break
    
print('Acabou')