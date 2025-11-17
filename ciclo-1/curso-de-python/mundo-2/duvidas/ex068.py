import random
print('-' * 35)
print('PAR OU ÍMPAR')
print('-' * 35)

escolhaNumUsuario = int(input('Digite um valor: '))
escolhaParOuImpUsuario = str(input('Par ou Ímpar? [P/I]  '))

par = escolhaNumUsuario % 2 == 0
impar = escolhaNumUsuario % 2 != 1
parImpar = [par, impar]
escolhaNumMaquina = random.choice(parImpar)