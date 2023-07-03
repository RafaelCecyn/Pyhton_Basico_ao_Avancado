# Try, except, else e finaly (Parte 2)

# a = 18
# b = 0
# c = a / b
try:
    a = 18
    b = 0
    print(b[1])
    c = a / b
except ZeroDivisionError:
    print('Error divisão por zero')
except NameError:
    print('Nome b não está definido')
except (TypeError,IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:',error)
    print(error.__class__.__name__)
except Exception:
    print('Erro genérico')