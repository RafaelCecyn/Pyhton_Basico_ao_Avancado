'''
Introdução ao desempacotamento
'''

nome1,nome2,nome3 = ['Maria','Anna','Flávia']
print(nome1,nome2,nome3)

# Pegar só o primeiro nome e ignorar os outros

nome1,*_ = ['Maria','Anna','Flávia']
print(nome1,_)