soma = 0
contador = 0
numero = 0
while numero != 999:
    numero = int(input('digite um número[para quando digitar 999]: '))
    soma += numero
    contador += 1
print(f'a soma de todos esses {contador - 1} números é {soma - 999}')
