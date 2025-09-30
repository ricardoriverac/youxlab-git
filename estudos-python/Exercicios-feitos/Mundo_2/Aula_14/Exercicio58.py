import random
numeroDaMaquina = random.randint(0,10)
tentativas = 0
acertou = False
while not acertou:
    meuNumero = int(input('Tente adivinhar o número entre 0 e 10 que a máquina está pensando: '))
    tentativas += 1
    if meuNumero == numeroDaMaquina:
        acertou = True
    else:
        if meuNumero > numeroDaMaquina:
            print ('Tente novamente é um número menor')
        elif meuNumero < numeroDaMaquina:
            print ('Tente novamente é um número maior')
print (f'Você acertou! Parabéns teve {tentativas} tentativas!')