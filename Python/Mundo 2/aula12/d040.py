nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5.0:
     print(f'Sua média é {media}, você está REPROVADO!')
elif 5.0 <= media <= 6.9:
     print(f'Sua média é {media}, você está de RECUPERAÇÃO!')
elif media >= 7.0:
     print(f'Sua média é {media}, você está APROVADO!')
