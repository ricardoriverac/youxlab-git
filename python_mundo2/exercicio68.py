import random
sn = 0                                                                #vezes que o jogador ganhou
escolhadog = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                         #escolha do computador
na = 0                                                                   # número escolhido pelo jogador
of = 0                                                                  #opção final
opçãof = 0
escolhadepi = str(input('você escolhe [PAR/IMPAR]: ')).upper()
if escolhadepi == 'PAR' :
    while of % 2 == 0 :
        ne = int(input('Digite um número de 1 até 10 :'))                      #número escolhido
        na = ne
        sn = sn + 1                                                        
        opçãoe = random.choice(escolhadog)
        opçãof = opçãoe + ne
        of = opçãof
        print ('a escolhida pelo computador é {}, a pelo jogador é {} e a soma é {}' .format(opçãoe, ne , of))
else:
     while of % 2 != 0 :
        ne = int(input('Digite um número de 1 até 10 :'))                      #número escolhido
        na = ne
        sn = sn + 1                                                        
        opçãoe = random.choice(escolhadog)
        opçãof = opçãoe + ne
        of = opçãof
        print ('a escolhida pelo computador é {}, a pelo jogador é {} e a soma é {}' .format(opçãoe, ne , of))