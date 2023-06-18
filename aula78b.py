# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Luiz')
s1.add(1)
# s1.add(1,2) Erro ao enviar no add dois argumetos
# s1.update('Olá Mundo') # {1, 'l', 'd', 'o', 'u', 'á', ' ', 'n', 'Luiz', 'O', 'M'}
s1.update(('Olá Mundo',1,2,3,4)) #{1, 2, 3, 4, 'Luiz', 'Olá Mundo'}
# s1.clear()
s1.discard('Olá Mundo') # Remove somente o 'Olá Mundo' {1, 2, 3, 4, 'Luiz'}
print(s1)