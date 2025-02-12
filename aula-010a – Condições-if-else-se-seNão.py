#Aula 10 – Condições (if, else, se, seNão)

#esturura sequêncial de um programa em python é seguir a ordem de cima para baixo e da esquerda para a direita
#usamos a represntação de um fluxograma para representar a estrutura de um programa e a lógica de programação
#representaçào identada de um programa em python alinha o código de acordo com a lógica de programação apertando tab
#boclo verdaeiro é o valor que é sempre verdadeiro
#bloco falco é o valor que é sempre falso
#estrutura CONDICIONAL SIMPLES : if (se)
#estrutura condicional composta: if e else (se e se não)

# Não podemos esquecer dos dois pontos : no final da linha de condição if e else

#-----------------------------------Condição if (): e else: -----------------------------------
#if carro.esquerda(): #se o carro for para a esquerda
#else: #se não for para a esquerda


#-----------------------------------------------------------------------------------------------------------------------
#Exemplo 1:
'''
tempo = int(input('Quantos anos tem seu carro? ')) #input é uma função que recebe um valor digitado pelo usuário #int é uma função que converte o valor digitado para inteiro
if tempo <=3: #se o tempo for menor ou igual a 3 anos
    print('Seu carro é novo')
else:
    print('Seu carro é velho')
print('---FIM---')
'''

#-----------------------------------------------------------------------------------------------------------------------
#Exemplo 2:
'''
idade = int(input('Quantos anos você tem? ')) #int é uma função que converte o valor digitado para inteiro
if idade >= 18: #se a idade for maior ou igual a 18 anos
    print('Você é maior de idade')
else:
    print('Você é menor de idade')
print('---FIM---')
'''
'''
condição
var = int(input())
if var operador : 
else:
    print('---FIM---')
'''

#--------------------------------------------Estrutura-composta ou simples ---------------------------------------------
#Exemplo 3:

'''
#simples apenas if
nome = str(input('Qual é o sue nome? ')) #str é uma função que converte o valor digitado para string
if nome == 'Gustavo':#se o nome for igual a Gustavo É  VERDADEIRO
    print('Que nome bonito você tem!')
print('Bom dia, {}!'.format(nome))
'''
#------------------------------------------------------------
'''
#composto if e else
nome = str(input('Qual é o sue nome? ')) #str é uma função que converte o valor digitado para string
if nome == 'Gustavo':#se o nome for igual a Gustavo É  VERDADEIRO
    print('Que nome bonito você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
'''
#----------------------------------------------Media de notoas estrutura composta --------------------------------------
#Exemplo 4:

n1 = float(input('Digite a primeira nota: ')) #float é uma função que converte o valor digitado para real
n2 = float(input('Digite a segunda nota: ')) #float é uma função que converte o valor digitado para real
m = (n1 + n2) / 2 #média das notas
print('Sua média foi {:.1f}'.format(m))
if m >= 80:
    print('sua nota é boa')
else:
    print('Sua nota é um lixo')
print('Tenha um bom dia !!!')

#blocos de comando em python são identificados pela identação em java scrip o blobo de comando é dentro das chaves "{}"

#--------------------------------------------condição simplificada------------------------------------------------------

print('*Parabéns' if m >= 80 else'*Estude mais +++')


