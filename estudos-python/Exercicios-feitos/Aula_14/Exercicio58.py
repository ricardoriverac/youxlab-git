import random
meuNumero = int(input('Tente adivinhar o número entre 0 e 10 que a máquina está pensando: '))
numeroDaMaquina = random.randint(0,10)
tentativas = 0
while meuNumero != numeroDaMaquina:
    print ('Tente denovo')
    meuNumero = int(input('Tente adivinhar o número novamente entre 0 e 10 que a máquina está pensando: '))
    numeroDaMaquina = random.randint(0,10)
    tentativas += 1
print (f'Você acertou! Parabéns teve {tentativas} tentativas!')