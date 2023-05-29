# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

def duplica(x):
    return x * 2

def triplica(x):
    return x * 3

def quadruplica(x):
    return x * 4

dobro = duplica(2)
triplo = triplica(2)
quadruplo = quadruplica(2)

print(dobro, triplo, quadruplo)

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))