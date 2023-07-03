# Yield from

def generator():
    yield 1
    yield 2
    yield 3
    
    
def generator2():
    yield from generator()
    yield 4
    yield 5
    yield 6
    
    
g = generator2()
for n in g:
    print(n)