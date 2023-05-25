# Função format

a = 'Luiz'
b = 'Rafa'
c = 'Cris'

formato = 'a={}, b={},c={}'.format(a,b,c)

# Format por posição
formato = 'b={1}, a={0},c={2}'.format(a,b,c)

print(formato)