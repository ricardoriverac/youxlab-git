lista=[]
resposta =""
while resposta in "S":
    num=int(input("Adicione um valor: "))
    if num not in lista:
        lista.append(num)
    else:
        print("Esse numero ja existe")
    resposta=str(input("Deseja continuar? [S/N]")).upper()
    if resposta == "N":
        break
print(sorted(lista))