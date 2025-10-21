numero = 0
total = 0 
acumulador = 0 
while numero != 999:
    numero = int(input('Digite um numero:([999] para parar'))
    if numero != 999:
        total += 1
        acumulador += numero
    print(f'Voce digitou {total} vezes e a soma deles é {acumulador}')
