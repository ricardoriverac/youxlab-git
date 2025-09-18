idade = int(input('Qual ano você nasceu? '))                           #iano de nascimento do jovem
conidade = 2025-idade                                                  #idade do jovem
if conidade > 18:
    tidade = conidade - 18                                             #tempo que se passou desde o tempo de se alistar
    print ('você tem {} anos,se passaram {} anos desde que você tinha 18 anos, hora de se alistar já passou!'. format (conidade, tidade))
elif conidade < 18 :
    tidade2 = 18 - conidade                                             #tempo que falta para se alistar
    print ('Você ainda tem {} anos,faltam {} anos para você se alistar, ainda não é hora de se alistar' .format(conidade, tidade2))
elif conidade == 18 :
    print ("Você tem {} anos, este é o ano certo para se alistar!".format(conidade))