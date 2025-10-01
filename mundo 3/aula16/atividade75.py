#numero = int(input('digite um numero: ' ))
resto = 0
minha_tupla = ()
for c in range(0,4):
    numero = int(input('digite um numero: ' ))
    minha_tupla += (numero,)
print(minha_tupla)

print(minha_tupla.count(9))
if 3 in minha_tupla:
    print(minha_tupla.index(3))
else:
    print("3 nao esta na tupla")
par = 0 
for numero in minha_tupla:
    if numero % 2 == 0:
        par += 1
print(par)         