'''
# O INTERNO TEM ACESSO AO EXTERNO, MAS O EXTERNO NÃO TEM ACESSO AO INTERNO
Escopo de funções em Python
Escopo significa o local onde aquele códgio pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo
ser a mesma do escopo interno
'''

x = 1 # Se for definido após a chamada da função da erro


def escopo():
    def outra_funcao():
        y = 2
        print(x, y)
    outra_funcao()
    print(x)
    

escopo() # 1 2     1


def escopo():
    x = 10
    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)
    

escopo() #  11 2    10 # Outro local da memória call stack (pilhas)
print(x) #  1



def escopo():
    global x # Agora o x global é 10
    x = 10
    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)
    

escopo() #  11 2    10
print(x) #  10




