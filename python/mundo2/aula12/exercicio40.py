nota1=float(input('Primeira nota: '))
nota2=float(input('Segunda nota: '))
media=(nota1+nota2)/2
print(f'Tirando {nota1} e {nota2}, a meida do aluno é {media}')
if 7>media>=5 and media<7:
    print(F'O aluno esta de RECUPERAÇÃO.')
elif media<5:
    print('O aluno esta REPROVADO.')
elif media >7:
    print('O aluno esta APROVADO.')