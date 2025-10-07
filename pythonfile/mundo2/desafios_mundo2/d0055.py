menorpeso = 1000
maiorpeso = 0
for c in range (0,5):
    peso = float(input('Digite seu peso: '))
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso:
        menorpeso = peso
print(f'O maior peso é {maiorpeso}\n e o menor peso é {menorpeso}.')