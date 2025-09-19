velocidade = float(input('Qual velocidade você está percorrendo? '))
multa = (velocidade-80) *7
if velocidade>80:
    print('Você está acima de 80km/h, portando está MULTADO por passar do limite permitido...')
    print(f'Você pagará uma MULTA de R${multa}!')
else:
    print('Esta tudo certo! Tenha um bom dia!')


