ano = int(input("digite algum ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("esse ano e bissexto")
else:
    print("esse ano nao e bissexto")

