'''
Repetições
while (enquanto)
Executa uma ação enquanto a condição é VERDADEIRA
Loop infinito -> Quando um código não tem fim
'''

qtde_linhas = 5
qtde_colunas = 5

linha = 1

while linha <= qtde_linhas:
    coluna = 1
    while coluna <= qtde_colunas:
        print(linha, coluna)
        coluna+=1
    linha += 1
    
print('Acabou')