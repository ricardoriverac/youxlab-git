km = float(input('Digite o tanto de km será percorrido na sua viagem: '))
preço= km * 0.50
preço2 = km * 0.45
if km <= 200:
     print("O valor da sua passagem é de R${}".format(preço))
else: 
     print("Sua viagem é mais longa, então o valor da sua passagem é de R${}".format(preço2))