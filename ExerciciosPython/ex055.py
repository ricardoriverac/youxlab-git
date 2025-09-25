maiorPesoCount = float(input("Digite o peso da 1ª pessoa: "))
menorPesoCount = maiorPesoCount
for c in range(2, 6):
    peso = float(input(f"Digite o peso da {c}ª pessoa: "))
    if peso > maiorPesoCount:
        maiorPesoCount = peso
    elif peso < menorPesoCount:
        menorPesoCount = peso

print(f"\nO maior peso lido foi: {maiorPesoCount:.2f} kg")
print(f"O menor peso lido foi: {menorPesoCount:.2f} kg")