# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations,product

pessoas = [
    'João', 'Joana','Luiz','Letícia'
]
 
camisetas = [
    ['preta','branca'],
    ['p','m','g']
]

# print(*list(combinations(pessoas,2)),sep='\n') # Combinação 4, 2 a 2
# print()
# print(*list(permutations(pessoas,2)),sep='\n') # Permutação 4, 2 a 2

print(list(product(*camisetas))) # [('preta', 'p'), ('preta', 'm'), ('preta', 'g'), ('branca', 'p'), ('branca', 'm'), ('branca', 'g')]





