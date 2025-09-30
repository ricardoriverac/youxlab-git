contagem = 0
tupla = ()
contagemPar = 0
for valor in range(4):
    resposta = int(input(f"Digite os valores {valor}: "))
    tupla += (resposta,)
for a in tupla:
    if a == 9:
        contagem += 1
print(f"O numero 9 aparece {contagem} vezes!")
for index,d in enumerate(tupla):
    if d == 3:
        print(f"A posição do numero 3 é: {index}")
for c in tupla:
    if c % 2 == 0:
        contagemPar += 1
print(f"A quantidade de pares é {contagemPar}")