#imprt comando para importar bibliotecas "sempre na primeira linha "
#importando toda a biblioteca
import math #importa o modulo math ou biblioteca
#importando apenas dois itens
#from math import sqrt,floor

num = int(input('Digite um número: '))
raiz = math.sqrt(num) #ponto abre as bibliotecas
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) #math.ceil(raiz) calcula raiz e arredonda para cima com ceil!

#outra forma de print para o mesmo código
#print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
