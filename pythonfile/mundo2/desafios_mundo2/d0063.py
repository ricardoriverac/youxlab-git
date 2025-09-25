print('Sequencia de fibonacci')
numero = int(input('Quantos termos você quer mostrar?: '))
primeiroTermo = 0
segundoTermo = 1
print(f'{primeiroTermo} {segundoTermo}', end='')
contador = 3
while contador <= numero :
    termo3 = primeiroTermo + segundoTermo
    print(f' {termo3}', end='')
    primeiroTermo = segundoTermo
    segundoTermo = termo3
    contador += 1 
print(' FIM')
