# Mapeamento de dados em list comprehension

produtos = [
    {'nome':'p1','preco':20, },
    {'nome':'p2','preco':10, },
    {'nome':'p3','preco':30, },
]

novos_produtos = [
    produto
    for produto in produtos
]

print(novos_produtos) # [{'nome': 'p1', 'preco': 20}, {'nome': 'p2', 'preco': 10}, {'nome': 'p3', 'preco': 30}]
print(*novos_produtos,sep='\n') # {'nome': 'p1', 'preco': 20}
                                # {'nome': 'p2', 'preco': 10}
                                # {'nome': 'p3', 'preco': 30}
                                
                                
novos_produtos = [
    produto['nome']
    for produto in produtos
]

print(novos_produtos) # ['p1', 'p2', 'p3']

novos_produtos = [
    {'nome': produto['nome'], 'preco': produto['preco']}
    for produto in produtos
]
print(novos_produtos)  # [{'nome': 'p1', 'preco': 20}, {'nome': 'p2', 'preco': 10}, {'nome': 'p3', 'preco': 30}]



novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]
print(novos_produtos) # [{'nome': 'p1', 'preco': 21.0}, {'nome': 'p2', 'preco': 10.5}, {'nome': 'p3', 'preco': 31.5}]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(novos_produtos) # [{'nome': 'p1', 'preco': 20}, {'nome': 'p2', 'preco': 10}, {'nome': 'p3', 'preco': 31.5}]