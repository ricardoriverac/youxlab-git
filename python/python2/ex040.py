nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota :'))
media = (nota1 + nota2) /2
if media > 5.0:
    print(f'Voce esta REPROVADO, sua media foi {media}')
elif media >= 7:
    print(f'Voce esta APROVADO, sua media foi {media}')
else:
    print(f'Voce esta de recuperacao, sua media foi de {media}')