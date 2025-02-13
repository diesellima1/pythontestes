

#condição simples
print('\033[33m condição simples\033[m')  # letra amarela

nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
print('Tenha um bom dia {}!'.format(nome))

#------------------------------------------

#condição composta
print('\033[33m condição composta \033[m')  # letra amarela

nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
else:
    print('Seu nome é normal.')
print('Tenha um bom dia {}!'.format(nome))

#------------------------------------------

# condição aninhada com if elif else
print('\033[33m condição aninhada!\033[m')  # letra amarela

nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': # or
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claúdia Jessica Juliana':     #in
    print('Belo nome Feminino!')
else:
    print('Seu nome é normal.')
print('Tenha um bom dia {}! \nFIN.'.format(nome))













