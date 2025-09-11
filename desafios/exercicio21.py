import random

# 1. O computador "pensa" num número de 0 a 5
numero_aleatorio = random.randint(0, 5)

# 2. Pede ao utilizador para digitar o seu número
try:
    palpite_utilizador = int(input("Adivinhe um número entre 0 e 5: "))

    # 3. Compara os números e exibe o resultado
    if palpite_utilizador == numero_aleatorio:
        print("Parabéns, você acertou! O número era", numero_aleatorio)
    else:
        print("Que pena, você errou. O número era", numero_aleatorio)