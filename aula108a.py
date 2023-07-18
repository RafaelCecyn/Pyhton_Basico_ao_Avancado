# count é um iterador sem fim (itertools)
from itertools import count


c1 = count(8,8) # Inicia do 8, passo 8
r1 = range(8,100,8) # Inicia do 8, passo 8

# print(next(c1)) # 0
# print(next(c1)) # 1

# Verifica se um objeto é um iterator
print('c1',hasattr(c1, '__iter__')) # c1 True é um iterável
print('c1',hasattr(c1, '__next__')) # c1 True é um iterator, pois tem o método NEXT
print('r1',hasattr(r1, '__iter__')) # r1 True é um iterável
print('r1',hasattr(r1, '__next__')) # r1 False não é um iterator


print('count')
for i in c1:
    if i >= 100:
        break
    
    print(i)
    
print()
for i in r1:
    print(i)