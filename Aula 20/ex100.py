from random import randint
numeros = []
def sorteia():
	for i in range (1, 6):
		numero1 = randint(0, 20)
		numeros.append(numero1)
		
		
def somaPar():
	soma = 0
	for numero in numeros:
		if numero % 2 == 0:
			soma += numero
	print(f"Os números sorteados foram: {numeros} e a soma dos valores PARES é: {soma}")
print('*' * 80)

sorteia()
somaPar()
