from random import randint
numeroMenor = 1000
NumeroMaior = 0
numero = ()
for numeros in range(5):
    numeroAleatorio = randint(1, 1000)
    numero += (numeroAleatorio,)
    print(numeroAleatorio)
print(numero)
for digito in numero:
    if digito < numeroMenor:
        numeroMenor = digito
    if digito > NumeroMaior:
        NumeroMaior = digito
print(f'O número MAIOR é {NumeroMaior}!')
print(f'O número MENOR é {numeroMenor}!') 