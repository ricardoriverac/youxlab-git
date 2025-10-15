def fatorial(numero, comeco):

	if(numero > 0):
		if(comeco == True):
			print(end ='' f'{numero} x ' if numero > 1 else f'{numero} = ');
			return numero * fatorial(numero - 1, True);
		else:
			return numero * fatorial(numero - 1, False);
	else:
		return 1;

print(fatorial(5, True))