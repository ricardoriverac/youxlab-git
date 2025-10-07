from random import randint

valores = ()
maiorValor = 0
menorValor = 1000
for contagem in range(5):
    numero = randint(0, 999)
    valores = valores + (numero,)

for v in valores:
    if v > maiorValor:
        maiorValor = v
    if v < menorValor:
        menorValor = v
print(f'Os valores são {valores}')
print(f'O maior valor é {maiorValor}')
print(f'O maior valor é {menorValor}')