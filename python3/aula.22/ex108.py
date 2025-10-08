import moeda
listapessoas = []
dobro = antecessor = sucessor = metade = real = 0
continuar = 'S' 

while continuar == 'S':
  numero = float(input('Digite um valor: '))
  listapessoas.append(numero)
  print(listapessoas) 

  for v in listapessoas:
    real = moeda.real(v)
    metade = moeda.metade(v)
    dobro = moeda.dobro(v)
    antecessor = moeda.diminuir(v)
    sucessor = moeda.aumentar(v)
  continuar = str(input('Deseja continuar[S/N]? ')).upper()

print(f'O antecessor do numero {v} é {antecessor} e o seu sucessor é {sucessor}')
print(f'O dobro do valor {v} é : {dobro} e sua metade é : {metade}')
print(f'O valor {v} em reais : {real}')
   

