nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
smedia = nota1 + nota2
media = smedia / 2
if media > 7.0 :
    print ('PARABÉNS!! você passou, sua media é {}' . format(media))
elif media < 5.0 :
    print ('PESSIMO!! você foi reprovado, sua media é {}'.format(media))
elif media > 5.0 and media < 6.9 :
    print ('infelismente você ficou de recuperação, estude mais da prôxima, sua media é {}'.format(media))