numero = int(input('Digite um número: '))
resultado = 0
numeroMaior = numero
numeroMenor = numero - 1
while numero > 0
    if numero == numeroMaior:
        resultado = numeroMaior * numeroMenor
        numero -= 1
    else:
        resultado = resultado *  numero
    numero -= 1
print(f'O resultado da fatorial é {resultado}')