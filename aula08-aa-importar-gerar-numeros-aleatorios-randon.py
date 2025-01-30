#gerar numeros aleatórios

import random
#num = random.random()             #função não escolhe os números
num = random.randint(1, 60) # função escolhe os números
print(num)


#importar  PyPI ajuda você a encontrar e instalar softwares desenvolvidos e
# compartilhados pela comunidade do Python.
import emoji
#pip install emoji
# Adiciona emoji à string usando a biblioteca emoji e a linguagem de alias
print(emoji.emojize('Olá, Mundo!!! :earth_americas:', language='alias'))



#OBSOLETO
'''
#use_aliases não é mais suportado nas versões mais recentes. Você pode usar language='alias'
#emoji importado manualmente "import emoju" lampada vermelha install packege emoji

import emoji
print(emoji.emojize('Olá, Mundo!!!:earth_americas:', use_aliases=True))
'''