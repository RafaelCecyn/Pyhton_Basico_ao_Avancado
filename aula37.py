'''
Repetições
while (enquanto)
Executa uma ação enquanto a condição é VERDADEIRA
Loop infinito -> Quando um código não tem fim
Continue -> Volta para o começo do laço
'''

contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6:
        print('Não quero mostrar o 6')
        continue
        
    if contador >= 10 and contador <= 27:
        print('Não quero mostrar',contador)
        continue
        
    print(contador)
    
    if contador == 40:
        break
    
print('Acabou')
        