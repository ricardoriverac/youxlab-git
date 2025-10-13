def fat(numero, comeco):

	if(numero > 0):
		if(comeco == True):
			print(end ='' f'{numero} x ' if numero > 1 else f'{numero} = ');
			return numero * fat(numero - 1, True);
		else:
			return numero * fat(numero - 1, False);
	else:
		return 1;

print(fat(5, True))