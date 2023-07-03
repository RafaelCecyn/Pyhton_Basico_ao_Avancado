# Try, except, else e finaly

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
except (TypeError,IndexError):
    print('Erro no tipo')
except Exception:
    print('Erro genérico')
    