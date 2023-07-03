# try, except, else e finally

try:
    print(1)
    # 8/0
except ZeroDivisionError:
    print('Dividiu por zero')
else:
    print('Não deu erro')
finally:
    # Sempre será executado
    print(2)