contador = 0 
soma = 0
while True:
    primeiroNumero = int(input('Digite um número [999 para parar]:'))
    if primeiroNumero == 999:
       break
    soma += primeiroNumero
    contador += 1

print('Você digitou {} números e a soma entre eles foi de {}'.format(contador,soma))
print('Programa encerrado')