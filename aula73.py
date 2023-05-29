'''
Higher Order Functions
Funções de primeira classe
'''

def saudacao(msg):
    return msg

saudacao_2 = saudacao # Possa atribuir uma variável a função e ela tem o mesmo lugar na memória que a função

v = saudacao_2('Olá')
print(v)




def saudacao(msg):
    return msg

def executa(funcao,msg):
    return funcao(msg)

v = executa(saudacao,'Bom dia') # Chamo a função dentro da função executa sem os ()
print(v)



def saudacao(msg,nome):
    return f'{msg}, {nome}!'

def executa(funcao,*args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)


print(
    executa(saudacao, 'Bom noite', 'Maria')
)