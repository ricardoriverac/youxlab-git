peso = float(input("digite seu peso kg: "))
altura = float(input("digite sua altura m: "))
imc = peso / (altura **2)
print(f"o imc dessa pessoa e de {imc:.1f}")
if imc < 18.5:
    print("voce esta abaixo do peso normal")
elif 18.5 <= imc < 25:
        print("voce esta na faixa de peso normal")
elif 25 <= imc < 30:
      print("voce esta em sobrepeso") 
elif 30 <= imc < 40:
      print("voce esta obeso")  
else:
      imc >= 40
      print("voce com obesidade morbida")        
