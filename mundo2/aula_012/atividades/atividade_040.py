'''
Cria um programa qua leia duas notas de um aluno e calcule sua média. mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo da 5.0: REPROVADO
Média entre 5.0 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
'''

#Resposta

nota = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))
media = ((nota + nota2) / 2)

if media >= 7.0 :
    print('você foi APROVADO!!')

elif media < 5.0 :
    print('você foi REPROVADO!!')

elif media >= 5.0 or media <= 6.9 : 
    print('você esta de RECUPERAÇÃO!!')