

#--------------------------------------------------código das cores!----------------------------------------------------

#\033[style;cor_do_texto;cor_do_background m  "033 funcina melhor no terminal que outros códigos!"m deve ser junto sem ponto e vírgula

#\033[0;33:44m

#-----------------------------Copy---------------------------------

#sem limite             print('\033[0;30;41m Seu texto aqui:')

#limitada              print('\033[1;31;43m Seu texto aqui: \033[m')

#--------------------

#copie e preencha a fórmula com os códigos abaixo

#..................................................
#>>>>>>>>>>>>>Código do estilo>>>>>>>>>>>>>>>>>>>>>
#0 nono "nada de estilo"
#1 Bold "estilo em negrito"
#4 Underline "sublinado"
#7 Negative  "ele inverte as cores"
#..................................................

#>>>>>>>>>>>>>Cor do texto>>>>>>>>>>>>>>>>>>>>>>>>
#30 branco
#31 vermelho
#32 verde
#33 amarelo
#34 azul
#35 magenta "lilas"
#36 ciano "azul claro"
#37 cinza
#..................................................

#>>>>>>>>>>>>>Cores do blackground>>>>>>>>>>>>>>>>>
#40 branco
#41 vermelho
#42 verde
#43 amarelo
#44 azul
#45 magenta "lilas"
#46 ciano "azul claro"
#47 cinza

#--------------------------------------------------cores prontas para usar----------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print('\033[31m Olá, Mundo vermelho!\033[m')  # letra vermelha
print('\033[1;31m Olá, Mundo vermelho negrito!\033[m') #vermelho bold
print('\033[32m Olá, Mundo Verde!\033[m')  # letra verde
print('\033[1;32m Olá, Mundo Verde negrito!\033[m')  # letra verde bold
print('\033[33m Olá, Mundo amarelo!\033[m')  # letra amarela
print('\033[1;33m Olá, Mundo amarelo negrito!\033[m')  # letra amarelo em negrito "Bold"
print('\033[4;34m Olá, Mundo azul sublinhado!\033[m')  #azul anderline  "sublinhado"
print('\033[1;4;34m Olá, Mundo azul sublinhado!\033[m')  #azul anderline  "sublinhado" com negrito "Bold"

#--------------------------------------------------cores selecionadas ----------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m !!!'.format(a, b))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#--------------------------------------------------arco iris -----------------------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print(
    '\033[30m Olá, Mundo Branco! \033[m'  # Branco
    '\033[31m Olá, Mundo Vermelho! \033[m'  # Vermelho
    '\033[32m Olá, Mundo Verde! \033[m'  # Verde
    '\033[33m Olá, Mundo Amarelo! \033[m'  # Amarelo
    '\033[34m Olá, Mundo Azul! \033[m'  # Azul
    '\033[35m Olá, Mundo Magenta! \033[m'  # Magenta (Lilás)
    '\033[36m Olá, Mundo Ciano! \033[m'  # Azul Claro
    '\033[37m Olá, Mundo Cinza! \033[m'  # Cinza
)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#..................................................outras formas........................................................

print('\033[1;31;43m Olá, Mundo!\033[m')    #balckground só no texto
print('\033[4;30;45m Olá, Mundo!\033[m')    #balckground só no texto



#            \033[;;m]
print('\033[0;30;41m texto####aqui 1') #fundo vermelho
print('\033[4;33;44m texto####aqui 2') #sublinhado
print('\033[1;35;43m texto####aqui 3') #35 texto magenta "lilas"
print('\033[30;42m texto####aqui 4')   #pulou o estilo
print('\033[m texto####aqui 5')        #padrão do terminal
print('\033[7;30m texto####aqui 6')    #inversão de cores



#existe mais códigos mas esse fuincinam melhor


#---------------------------------------------Instruções adicionais-----------------------------------------------------
#---------------------------------------------ANSI Escape Sequences-----------------------------------------------------

'''
As sequências de escape ANSI (ANSI Escape Sequences) permitem adicionar cores e estilos ao texto exibido no
terminal. Elas são amplamente suportadas em terminais modernos.
Aqui está uma lista com as cores principais (foreground e background) que podem ser usadas no terminal com
ANSI Escape Sequences:
### Estrutura Básica:
``` plaintext
\033[<código de estilo>;<código de cor>m
```
- `\033[` ou `\e[` indica o início da sequência de escape.
- `<código de estilo>` define como o texto será formatado (negrito, sublinhado, etc.).
- `<código de cor>` define a cor do texto ou fundo.
- `m` finaliza a sequência.

### Códigos de Estilo

| Código | Efeito |
| --- | --- |
| 0 | Reset/Normal |
| 1 | Negrito |
| 3 | Itálico |
| 4 | Sublinhado |
| 7 | Inverte as cores (texto e fundo) |
| 9 | Tachado |
### Cores do Texto (Foreground)

| Cor | Código |
| --- | --- |
| Preto | 30 |
| Vermelho | 31 |
| Verde | 32 |
| Amarelo | 33 |
| Azul | 34 |
| Magenta | 35 |
| Ciano | 36 |
| Branco | 37 |
| Cinza Claro | 90 |
### Cores de Fundo (Background)

| Cor | Código |
| --- | --- |
| Preto | 40 |
| Vermelho | 41 |
| Verde | 42 |
| Amarelo | 43 |
| Azul | 44 |
| Magenta | 45 |
| Ciano | 46 |
| Branco | 47 |
| Cinza Claro | 100 |
### Exemplo no Python:
Aqui está como você pode usar essas cores no Python:
``` python
# Exemplo de cores no terminal
print("\033[1;32mTexto em verde com negrito\033[0m")  # Negrito e verde
print("\033[4;31mTexto sublinhado em vermelho\033[0m")  # Sublinhado e vermelho
print("\033[7;34mTexto com cores invertidas: azul\033[0m")  # Azul invertido
print("\033[1;30;43mTexto em preto com fundo amarelo\033[0m")  # Fundo amarelo
```
No exemplo acima:
- `\033[1;32m` ativa a sequência: estilo `1` (negrito) e cor do texto `32` (verde).
- `\033[0m` retorna ao normal para não afetar outros textos subsequentes.

Essas combinações são úteis em scripts que necessitam personalizar a saída no terminal!
'''