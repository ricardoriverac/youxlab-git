primeirNumero = int(input('Digite um número para calcular seu Fatorial:'))
fatorial = 1
contador = 1 

while contador <= primeirNumero:
    fatorial  *= contador
    contador += 1
    print('O Fatorial de {}! x {}'.format(primeirNumero,fatorial))
