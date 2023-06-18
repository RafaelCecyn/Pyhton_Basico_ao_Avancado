# Sets - Conjuntos em Python (tipo set)
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno

# Criando um set
# set (iterável) ou {1,2,3}
s1 = set('Luiz')
print(s1, type(s1)) # {'i', 'z', 'L', 'u'} <class 'set'>
s2 = set() # vazio
print(s2) #set()
s3 = {1,2,3} # com dados
print(s3) # {1,2,3}
s4 = {[1,2,3]} # Erro