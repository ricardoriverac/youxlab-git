nota1 = float(input('Digite um valor de sua nota: '))
nota2 = float(input('Digite o valor de outra nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'REPROVADO! Sua média é {media}, infelizmente sua média não chegou em 5.0!')
elif media >= 5.0 and media <= 6.9:
    print(f'RECUPERAÇÃO! Sua média é {media}, você ainda tem chance de recuperar!')
elif media > 7.0:
    print(f'APROVADO! Sua média é {media}, está acima de 7.0, PARABÉNS!!!')