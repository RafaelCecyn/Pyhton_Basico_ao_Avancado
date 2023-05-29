'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao,nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar                               # Retorna o lugar da memória

s1 = criar_saudacao('Bom dia', 'Maria')
s2 = criar_saudacao('Boa noite', 'Jose')

print(s1) # 0x00000261E1E8A0C0
print(s2) # 0x00000261E1EBE020

print(s1()) # Closure é como se eu colocasse os parenteses do s1 dentro do saudar sem parênteses 'Bom dia', 'Maria', e como se chamasse o saudar que não precisa de argumento
print(s2()) # Closure é como se eu colocasse os parenteses do s1 dentro do saudar sem parênteses 'Boa noite', 'Jose', e como se chamasse o saudar que não precisa de argumento





def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar                               # Retorna o lugar da memória

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa noite')

print(s1('Anna'))  # Closure é como se eu colocasse os parenteses do s1 dentro do saudar sem parênteses 'Bom dia', 'Maria', e como se chamasse o saudar que agora precisa de argumento
print(s2('Alfredo')) # Closure é como se eu colocasse os parenteses do s1 dentro do saudar sem parênteses 'Boa noite', 'Jose', e como se chamasse o saudar que agora precisa de argumento