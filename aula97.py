# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está  e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path

import sys
import aula97_m # Este módulo se chama aula97_m

print('Este módulo se chama', __name__) # Este módulo se chama __main__
print(*sys.path,sep='\n')