velocidade = int(input('Em qual velocidade o carro estava: '))
if velocidade > 80 :
    valorm = velocidade - 80 
    valorm2 = valorm * 7
    print ('O seu carro estava acima da velocidade, o valor da multa sera {}R$' .format(valorm2))
else:
    print ('seu carro estava na velocidade permitida ')