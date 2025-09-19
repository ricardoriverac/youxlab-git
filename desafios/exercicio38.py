numero1 = float(input('Digite um numero qualquer: '))
numero2 = float(input('Digite um numero qualquer: '))
if numero1 > numero2:
    print (f'{numero1} é MAIOR que {numero2}')
elif numero2 > numero1:
    print(f'{numero2} é MAIOR que {numero1}')
else:
    print('Não existe valor igual, AMBOS são iguais')