# dir, hasattr, getattr em Python

string = 'Luiz'

print(string)

# hasattr verifica se existe o método

if hasattr(string,'upper'):
    print('Existe o upper')
    
    
# getattr executa o método

metodo = 'lower'

if hasattr(string,metodo):
    print('Existe o método lower')
    print(getattr(string,metodo)())
else:
    print('Não existe o método',metodo)