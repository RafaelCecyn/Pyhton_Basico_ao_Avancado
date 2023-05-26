'''
split e join comn list e str
split divide uma str em list
join junta uma list em str
strip remove espaços em branco antes e depois
rstrip remove espaços depois
lstrip remove espaços antes
'''

frase = 'Olha só que, coisa interessante'
lista_frases_cruas = frase.split(',')

lista_frases = []


for i,frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i])

print(lista_frases_cruas)
print(lista_frases)

frases_unidas = '-'.join(lista_frases) # '' -> indica como devo unir o meu iterável
print(frases_unidas)