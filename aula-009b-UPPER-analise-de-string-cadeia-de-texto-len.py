#analise de uma string
#len() retorna o tamanho da string (quantidade de caracteres) leando em consideração os espaços em branco
#len() é uma função que retorna um valor inteiro lean vem de length que significa comprimento
from itertools import count

#lean é muito utilizada em programação para verificar se uma string é vazia ou não
#lean pergunta qual é o comprimento da frase "string"

len('frase') #retorna 5

#----------------------------------------------Contando letras "a" na frase "frase"-------------------------------------

#count é uma função que mostra quanta letas "a" tem na frase "frase" nesse caso 1 letra "a"

#----------------------------------------------count com a função de quebra de linha------------------------------------
frase.count('o',0,13) #retorna 1 do zero ao 13 eu só tenho 1 letra "o"

#----------------------------------------------find quantas vezes ele encontrou ----------------------------------------

frase.find('ase') #retorna 3 começa a contar do zero e a palavra "ase" começa no 3 ou seja em "f" "r" "a" "s" "e"


#----------------------------------------------find que não foi encontrada retorna como -1  ----------------------------

fase.find('android') #retorna -1 porque não foi encontrado a palavra "android"

#----------------------------------------------operador in para verificar se existe se sim "True"-----------------------

'curso' in frase #retorna True porque a palavra "curso" existe na frase

#----------------------------------------------replace tocar ou reposicionar "ele substitui a string"-------------------

frase.replace('frase','curso') #retorna "curso" porque a palavra "frase" foi substituida por "curso"

#----------------------------------------------Upper é um metodo "que significa para cima (UP)"-------------------------

frase.upper() #retorna "FRASE" porque todas as letras foram convertidas para maiusculas
#upper() não pode esquecer dos parenteses

#----------------------------------------------Lower é um metodo "que significa para baixo (DOWN)"----------------------

frase.lower() #retorna "frase" porque todas as letras foram convertidas para minusculas

#----------------------------------------------Capitalize é um metodo "que significa capitalizar"-----------------------

frase.capitalize() #retorna "Frase" porque a primeira letra foi convertida para maiuscula

#----------------------------------------------Title é um metodo "que significa titulo"---------------------------------

frase.title() #retorna "Frase" porque a primeira letra de cada palavra foi convertida para maiuscula

#----------------------------------------------Strip é um metodo "que significa tirar"----------------------------------

frase.strip() #retorna "frase" porque ele remove os espaços em branco no inicio e no final da frase

#----------------------------------------------Rstrip é um metodo "que significa tirar da direita"----------------------

frase.rstrip() #retorna "frase" porque ele remove os espaços em branco no final da frase

#----------------------------------------------Lstrip é um metodo "que significa tirar da esquerda"---------------------

frase.lstrip() #retorna "frase" porque ele remove os espaços em branco no inicio da frase
# #L de left que significa esquerda

#----------------------------------------------Split é um metodo "que significa dividir"--------------------------------

frase.split() #retorna ['frase'] porque ele divide a frase em uma lista de palavras

#----------------------------------------------Join é um metodo "que significa juntar"----------------------------------

'-'.join(frase) #retorna "f-r-a-s-e" porque ele junta a frase com o caracter "-" entre cada letra

#----------------------------------------------Format é um metodo "que significa formatação"----------------------------

'{} é uma {}'.format('Python','linguagem') #retorna "Python é uma linguagem" porque ele substitui os {} pelos valores

