import importlib

import aula98_m

print(aula98_m.variavel_modulo)

# for i in range(10):
#     print(i)
#     import aula98_m # Só importa o módulo uma vez
    
# print('Fim')

for i in range(10):
    importlib.reload(aula98_m)
    print(i)
    
print('Fim')