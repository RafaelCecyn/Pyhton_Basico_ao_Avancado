# isinstance - para saber se o objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2],(1, 2),
    {0,1}, {'nome': 'luiz'}
]

# for item in lista:
#     print(item,isinstance(item,set)) #a False
#1 False
#1.1 False
#True False
#[0, 1, 2] False
#(1, 2) False
#{0, 1} True
#{'nome': 'luiz'} False

for item in lista:
    if isinstance(item,set):
        item.add(5)
        print(item,isinstance(item,set))
        
    elif isinstance(item,str):
        item.upper() # Não altera para maiúscula, porque minha string é imutável
        print(item.upper()) # Aqui transforma para maiúscula
        
    elif isinstance(item,(int,float)):
        print(item,item * 2)
    else:
        print(item)
        
    