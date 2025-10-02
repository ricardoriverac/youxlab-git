quantos = 0
lista = []
for c in range(0,6):
    numero = int(input("digite um numero: "))
    lista.append(numero)
print(lista)  
lista.sort(reverse=True) 
print(lista)
if 5 in lista:
    print("o valor 5  esta na lista") 
else:
    print(" o valor 5  nao esta na lisa")    