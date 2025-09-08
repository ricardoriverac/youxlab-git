km=int(input('Qual a distancia da sua viagem em km?: '))
viagem1=0.50
viagem2=0.45

if km<200:
   print("O valor a pagar é:" + str(km * viagem1))
else:
   print("O valor a pagar é: " + str(km * viagem2))
