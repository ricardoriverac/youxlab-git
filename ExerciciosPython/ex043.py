peso = float(input("Qual é o seu peso (em KG)? "))
altura = float(input("Qual é a sua altura (em metros)? "))
imc = peso / (altura ** 2)
print(f"O seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Você está ABAIXO do peso.")
elif imc > 18 and imc <= 25:
    print("Você está com o peso IDEAL.")
elif imc > 25 and imc <= 30:
    print("Você está com o peso SOBREPESO.")
elif imc > 30 and imc <= 40:
    print("Você está com o peso OBESIDADE.")
elif imc >= 40:
    print("Você está com o peso OBESIDADE MÓRBITA.")
else:
    print("Você está acima do peso.")