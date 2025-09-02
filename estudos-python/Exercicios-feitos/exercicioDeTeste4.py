#Indentificador d enúmeros ímpares e parescd
numero = int (input ('Escolha um número para descobrir se é ímpar ou par'))
resultado = (numero % 2)
if resultado == 0:
    print ('O número escolhido é par') 
else:
    print ('O número é ímpar')