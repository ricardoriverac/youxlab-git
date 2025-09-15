velocidade=float(input('Qual é a velocidade do carro atual? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade permitido que é 80km\h')
    multa=velocidade * 7
    print(f'Voce deve pagasr a multa no valor de {multa}')
print('Tenha um bom dia')    