nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Você foi reprovado! ')
elif 0.5 <= media <= 6.9:
    print('Você está de recuperação!')
else:
    print('Você foi aprovado!')