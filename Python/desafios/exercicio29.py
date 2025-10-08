velocidade = float(input('Qual a velocidade do seu carro em km/h: '))
km = velocidade - 80
multa = 7* km 
if velocidade > 80:
    print (f'Voce foi multado {multa}')
else:
    print ('Voce ta dentro do limite')