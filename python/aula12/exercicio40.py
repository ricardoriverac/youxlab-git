nota1 = float(input('Digite a NOTA 1: '))
nota2 = float(input('Digite a NOTA 2: '))
media = (nota1 + nota2)/2

if media <= 5.0:
    print(f'REPROVADO \nA média final é: {media}')
elif 5.0 < media <= 6.9:
    print(f'RECUPERAÇÃO \nA média final é: {media}')
elif media >= 7.0:
    print(f'APROVADO \nA média final é: {media}')