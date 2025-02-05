#tecnica de fatiamento de string, os caracteres sempre começa a contar do 0 e sempre  um a menos no final ! exemplo
#do 9 ao 13, ele vai do 9 ao 12, pois o 13 é exclusivo. isso se chama range !
#exemplo: texto = "Hello, World!"
#A string "Hello, World!" possui 13 caracteres, incluindo espaços e pontuação.
#exemplos de fatiamento de string

'''
texto = "Hello, World!"
fatia1 = texto[0:5]    # Resultado: "Hello" # ou texto[:5]
fatia2 = texto[7:12]   # Resultado: "World"
fatia3 = texto[:5]     # Resultado: "Hello" # inverso também funciona texto[5:]
fatia4 = texto[7:]     # Resultado: "World!"
fatia5 = texto[-6:-1]  # Resultado: "World"
fatia6 = texto[::2]    # Resultado: "Hlo ol!"
fatia7 = texto[::-1]   # Resultado: "!dlroW ,olleH"
fatia8 = texto[3:8:2] # Resultado: ",o"
fatia9 = texto[9::3] # Resultado: ",l" #começa no 9 e pula de 3 em 3 até o final da string



A técnica de fatiamento em Python permite acessar partes de uma string (ou de outras sequências, como listas e tuplas) usando a sintaxe de colchetes com índices. A sintaxe básica é `string[início:fim:passo]`, onde:

- `início` é o índice inicial (inclusivo).
- `fim` é o índice final (exclusivo).
- `passo` é a quantidade de passos entre os índices.

Exemplo:
```python
texto = "Hello, World!"
fatia = texto[0:5]  # Resultado: "Hello"
```

Neste exemplo, `texto[0:5]` retorna os caracteres do índice 0 ao 4.
'''
'''
texto = "Hello, World!"
fatia = texto[0:5]  # Resultado: "Hello"
'''