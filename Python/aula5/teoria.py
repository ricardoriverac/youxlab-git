# Curso Python #09 - Manipulando Texto
# frase = 'curso em video python'
# [Significa lista]


# FATIAMENTO
# frase = 'curso em video python'
# frase[9:13]
# é do 9 ao 13

# frase[9:]
# é do 9 até o final

# frase[:9]
# é do começo até o 9

# frase[9:21:2]
# é pra ir de dois em dois

# frase[9::3]
# começa no 9 e vai ate o final e vai pulando de 3 em 3

# len(frase)
# comprimento

# frase.count('o') 
# vai contar quantas vezes existe esse elemento dentro do parenteses

# frase.count('o',0,13) 
# vai considerar do 0 ao 12

# frase.find('deo') 
# find - encontrar / quantas vezes ele encontrou o elemento dentro dos parenteses

# frase.find('android')
# quando colocar um valor que não existe ele volta o valor de -1 

# 'curso'in frase
# se dentro da frase existe a palavra que está entre as 'aspas'


# TRANSFORMAÇÃO

# frase.replace('Python','Android')
# .replace():  executa a operação de substituição, então vai substituir o primeiro elemento, pelo segundo elemento

# frase.upper()
# tudo ficar em maiúsculo e o que já é continua 

# frase.lower()
# tudo ficar em minusculo e o que já é continua 

# frase.capitalize()
# vai jogar todos os caracteres para minusculo e só o primeiro caractere fica maiúsculo

# frase.title()
# vai analisar quantas palavras tem e vai colocar todas as primeiras letras dos caracteres em maiuscula 

# FRASE:  APRENDENDO PYTHON
# frase.strip()
# vai remover todos os espaços do início e do final

# frase.rstrip()
# trata pela direita, ou seja remove os espaços do lado direito

# frase.lstrip()
# trata pela esquerda, ou seja remove espaços do lado esquerdo


# DIVISÃO
# FRASE: CURSO EM VÍDEO PYTHON
# frase.split()
# vai pegar aonde tem espaços e vai colocar aspas e  a cada palavra vai reiniciar a contagem das letras 
# Exemplo1: C U R S O | P Y T H O N 
#           0 1 2 3 4 | 0 1 2 3 4 5 
# Exemplo2: Dividindo por espaço (padrão)
# texto = "Olá, mundo Python"
# partes = texto.split()
# print(partes)  # Saída: ['Olá,', 'mundo', 'Python']
  

# JUNÇÃO
# '-'.join(frase)
# vai colocar o '-' entre as palavras

# PRÁTICA
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])