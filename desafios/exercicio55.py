contadorMaiorpeso = 0
contadorMenorpeso = 1000
for c in range (5):
    peso = float(input(f'Digite o {c+1}ª peso: ')) 
    if peso > contadorMaiorpeso:
        contadorMaiorpeso = peso

    if peso < contadorMenorpeso:
        contadorMenorpeso = peso
print(f'O maior o peso foi {contadorMaiorpeso}, é o menor peso foi {contadorMenorpeso}')