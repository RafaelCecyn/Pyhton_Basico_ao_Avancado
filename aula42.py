frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum'
    
i = 0
qtde_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtde_apareceu_mais_vezes_atual = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i+=1
        continue
    
    if qtde_apareceu_mais_vezes < qtde_apareceu_mais_vezes_atual:
        qtde_apareceu_mais_vezes = qtde_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
        
    i+=1
    
print(letra_apareceu_mais_vezes,qtde_apareceu_mais_vezes)