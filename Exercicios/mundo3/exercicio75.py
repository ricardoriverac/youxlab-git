tupla_resposta = ()
contador = 0
contador_par = 0
for valores in range(4):
    resposta = int(input(f"Digite o {valores+1}ª valor: "))
    tupla_resposta += (resposta,)
for a in tupla_resposta:
    if a == 9:
        contador += 1
print(f"O numero 9 aparece {contador} vezes!")
for index,d in enumerate(tupla_resposta):
    if d == 3:
        print(f"A posição do numero 3 é: {index}ª")
for c in tupla_resposta:
    if c % 2 == 0:
        contador_par += 1
print(f"A quantidade de pares é {contador_par}")
