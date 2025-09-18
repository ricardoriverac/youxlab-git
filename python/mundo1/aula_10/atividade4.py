distancia = float (input("vc viajou quantos km:"))
if distancia < 200:
    viagem1 = distancia * 0.50
    print(f"voce vai pagar {viagem1} ")
else:
    viagem2 = distancia * 0.45
    print(f"voce vai pagar {viagem2}")    
