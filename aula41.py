# while / else
# o else é executado depois que o while for executado todo
# caso tenha um break no while ele pula o else

nome = 'Luiz Otavio'

i = 0

while i < len(nome):
    letra = nome[i]

    print(letra)
    i+=1
else: 
    print('Estou no else')
print('Fora do while')