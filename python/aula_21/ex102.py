'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial.
'''


def fat(numero, comeco):

	if(numero > 0):
		if(comeco == True):
			print(end ='' f'{numero} x ' if numero > 1 else f'{numero} = ')
			return numero * fat(numero - 1, True)
		else:
			return numero * fat(numero - 1, False)
	else:
		return 1

print(fat(5, True))