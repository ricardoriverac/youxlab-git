#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
med = (nota1 + nota2) / 2
if med >= 7.0:
     print(f'Nota tirada: {med}. Resultado: Aprovada(o)')
elif 5.0 <= med < 7.0:
    print(f'Nota tirada: {med} Resultado: Recuperação')
else:
    print(f'Você foi REPROVADA(O), estude mais!')