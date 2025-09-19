from random import randint
computador = randint(0, 5) #esse comando faz o computador pensar em um número 
print('Irei pensar em um número entre 0 e 5!') 
quem_está_jogando = int(input('Em que número estou pensando?')) #jogador tenta adivinhar 
if quem_está_jogando == computador:
    print('PARABÉNS! VOCÊ ME VENCEU!')
else:
    print(f'EU GANHEI! PENSEI NO NÚMERO {computador} E NÃO NO {quem_está_jogando}')