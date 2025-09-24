numero = int(input("digite um termo:"))
razao = int(input("digite uma razao:")) 
c = 1
while c < 10:
    pa = numero + (c - 1) * razao 
    print(f"{pa}")
    c = c + 1