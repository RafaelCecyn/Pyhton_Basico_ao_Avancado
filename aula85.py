# List comprehension com mais de um for

lista = []

for x in range(3):
    for y in range(3):
        lista.append((x,y)) # -> Passar como uma tupla
        
        
lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

lista = [
    [x for y in range(3)]
    for x in range(3)
]
# [[0, 0, 0], [1, 1, 1], [2, 2, 2]]    
print(lista)