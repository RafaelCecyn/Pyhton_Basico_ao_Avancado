__all__ = [
    'variavel',
    'soma'
]
# from modulo_b import falaOi -> O main não enxerga a importação
from aula99_package.modulo_b import falaOi

variavel = 'alguma coisa'

def soma(x,y):
    return x + y


falaOi()
