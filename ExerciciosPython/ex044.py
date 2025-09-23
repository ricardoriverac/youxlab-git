# 1. Pedir ao utilizador o peso e a altura
peso = float(input("Qual é o seu peso (em KG)? "))
altura = float(input("Qual é a sua altura (em metros)? "))

# 2. Calcular o IMC
# A fórmula do IMC é peso dividido pela altura ao quadrado.
# Em Python, ** 2 eleva o número ao quadrado.
imc = peso / (altura ** 2)

# 3. Exibir o resultado do IMC
print(f"O seu IMC é: {imc:.2f}") # Formata para 2 casas decimais

# 4. (Opcional) Classificar o IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com o peso normal.")
else:
    print("Você está acima do peso.")