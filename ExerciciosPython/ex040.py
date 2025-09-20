nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f'Sua nota foi um {media :.2f}! PARABÉNS, VOCÊ ESTÁ APROVADO!!!!')
elif media  <= 6.9 and 5.0:
    print(f'Sua nota foi {media :.2f}! VOCÊ ESTÁ DE RECUPERAÇÃO!\nEstude mais da próxima vez!!!')
elif media < 5.0:
    print (f'Sua nota foi {media :.2f} VOCÊ ESTÁ REPROVADO!!!!')