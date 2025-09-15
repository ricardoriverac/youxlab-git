vcasa = float(input('qual o valor da casa? '))
vsalario = float(input('qual o valor do seu salário? '))
qanos = int(input('por qunatos anos você vai pagar a casa? '))
meses = qanos*12
parcelas = vcasa/meses
valorde30 = vsalario*30/100
if parcelas < valorde30:
    print ("Você podera comprar a casa!O valor que você pagara mensalmente sera {} ".format(parcelas))
else :
    print('infelismente você não recebe o suficiente para conseguir comprar a casa')