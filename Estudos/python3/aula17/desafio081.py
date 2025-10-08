import random
continuacao= 'dsad'
lista=list()
while continuacao not in 'N':
    numero=int(input('Digite um valor: '))
    lista.append(numero)
    continuacao= str(input('Você quer continuar? [S/N]').upper())
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
numeroAleatorio= random.randint(0, 100)
if numeroAleatorio in lista:
    print(f'O valor {numeroAleatorio} está na lista!')
else:
    print(f'O valor {numeroAleatorio} não está presente na lista!')