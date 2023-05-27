'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar ou listar
valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
'''
import os
lista = []

while True:
    print('Selecione uma opção ')
    escolha = input('[i]nserir [a]pagar [l]istar [s]air ')
    
    if escolha == 's':
        print('Você saiu')
        break
    elif escolha == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif escolha == 'a':
        os.system('cls')
        try:
            indice = input('Escolha um indice para apagar ')
            indice = int(indice)
            lista.pop(indice)
        except ValueError:
            print('Por favor digite um int. ')
        except IndexError:
            print('Índice não existe na lista')
        except:
            print('Não é possível apagar')
    elif escolha == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')
        for i, nome in enumerate(lista):
            print(i,nome)