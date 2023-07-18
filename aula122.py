# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self,nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando')
        
fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca) # Estou acessando a CLasse passando para ela o objeto fusca Fusca está acelerando
# print(fusca.nome)

celta = Carro('Celta')
celta.acelerar()
Carro.acelerar(celta) # Estou acessando a CLasse passando para ela o objeto celta Celta está acelerando
# print(celta.nome)