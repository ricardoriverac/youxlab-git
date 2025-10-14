valor = int(input("Quanto você quer sacar? R$"))
for cedula in [50, 20, 10, 1]:
    quantidade = valor // cedula 
    valor %= cedula
    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R${cedula}")