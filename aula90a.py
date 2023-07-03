import sys

# Generator expression, Iterables e Iteractors em Python
iterable = ['Eu','Tenho','__iter__']
iterator = iter(iterable) # tem __iter__ __next__
lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista)) # 85176 Bytes
print(sys.getsizeof(generator)) # 200 Bytes

print(next(generator)) # 0
print(next(generator)) # 1
print(next(generator)) # 2

print(generator)