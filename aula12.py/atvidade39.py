idade = int(input("digite sua idade: "))
tempo = 18 - idade
if idade < 18:
    print(f"voce nao precisa se alistar,falta {tempo}anos ")
elif idade == 18:
    print("voce tem que se alistar nesse ano")
else:
    idade > 18
    print(f"ja passou do tempo do alistamento,se passaram {tempo} anos ")       
