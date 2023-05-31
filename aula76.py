'''
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par "chave" e "valor".
Chaves podem ser considerados como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float,  bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário
Usamos as chaves {} ou a classe dict para criar dicionários
Imutáveis: str,int,float,bool,tuple
Mutáveis: dict,list
'''

pessoa_2 = dict(name='Rafa')
print(pessoa_2)

pessoa = {
    'nome':'Luiz',
    'sobrenome':'Otávio'
}
print(pessoa['nome'])

pessoa_3 = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra tal', 'número': 321},
        ],
}

for chave in pessoa_3:
    print(chave,pessoa_3[chave])