#Calcula quantos centimetros e milimetros tem na quantidade de metros escolhida
medidaEmMetros = float (input ('Insira em metros o tamanho do objeto '))
medidaEmCentimetros = (medidaEmMetros * 100)
medidasEmMilimetros = (medidaEmMetros * 1000)
print ('A quantidade de centímetros e milímetros em {}m é de {}cm e {}mm'.format(medidaEmMetros,medidaEmCentimetros,medidasEmMilimetros))