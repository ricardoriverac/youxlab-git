#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = float(input('Digite o primeiro termo da P.A: '))
razao = float(input('Digite a razão da P.A: '))
print('Os 10 primeiros termo da P.A são: ')
termo_atual = primeiro_termo
for i in range(10):
    print(f"Termo {i + 1}: {termo_atual}")
    termo_atual += razao
