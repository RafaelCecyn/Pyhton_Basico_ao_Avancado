# Generator expression, Iterables e Iteractors em Python
iterable = ['Eu','Tenho','__iter__']
iterator = iter(iterable) # tem __iter__ __next__
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


iter_2 = iterable.__iter__()