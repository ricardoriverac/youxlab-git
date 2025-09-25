print ('O computador escolheu um número de 1 até 10 (:')
ne = 0                                              #numero escolhido
import random 
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = random.choice(numero)
print (escolhido)
while ne != escolhido :
    ne = int(input('Digite um número para tentar adivinhar: '))
print ('BÁAAAAAA! VOCÊ ACERTOU!! O número era {}' .format(ne))