import moeda
listapessoas = []
dobro = antecessor = sucessor = metade = 0
for c in range(0,5):
   numero = int(input('Digite um valor: '))
   listapessoas.append(numero)
   print(listapessoas)

metade = moeda.metade(numero)
dobro = moeda.dobro(numero)
antecessor = moeda.diminuir(numero)
sucessor = moeda.aumentar(numero)
print(f'O antecessor do numero {numero} é {antecessor} e o seu sucessor é {sucessor}')
print(f'O dobro do valor {numero} é {dobro} e sua metade é {metade}')