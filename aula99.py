from sys import path

import aula99_package.modulo
from aula99_package import modulo
from aula99_package.modulo import soma
from aula99_package.modulo import *

# print(*path,sep='\n') # C:\Users\rafael.cecyn\Desktop\Curso_de_Python -> Principal


print(soma(2,3))
print(aula99_package.modulo.soma(2,3))
print(modulo.soma(2,3))