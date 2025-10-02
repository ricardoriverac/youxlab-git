lista = ()
lista_pesados = []
lista_leves = []
contador = 0
contador_peso = 0
loop = True


while loop:
    nomes = str(input("Digite seu nome: "))
    peso = float(input("Digite seu peso: kg "))
    lista += (nomes, peso)
    contador += 1
    contador_peso += peso
    pergunta = str(input("Deseja continuar? [S/N]: ")).upper()
    if pergunta == "N":
        loop = False

print("nome/peso")
for ordem in range(0,len(lista), 2):
   print(lista[ordem], " -> ",lista[ordem+1])
media = contador_peso/contador
for i in range(0,len(lista)):
    peso = lista[i][1]
    if peso > media:
        lista_pesados.append(peso)
    else:
        lista_leves.append(peso)
   
print(f"A quantidade de pessoas cadastradas são: {contador}")
print(f"E o peso mais pesado é: {lista_pesados}") 
print(f"A pessoa mais leve é: {lista_leves}")