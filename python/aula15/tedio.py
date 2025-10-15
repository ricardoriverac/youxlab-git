continuar = 'S'
qtd = contando = count = 0
while continuar in 'Ss':
	contando = int(input('Digite qualquer coisa: '))
	continuar = str(input('Você quer continuar? [S/N] \n'))
	count +=1
	if count > 5:
		print('Por quê?')
	else:
		print('hm')
print('tchau')
