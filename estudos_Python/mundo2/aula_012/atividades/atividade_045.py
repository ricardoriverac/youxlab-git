'''
Cria um programa que faça o computador jogar Jokenpô com você.
'''

#Resposta
import random

print('''
    PEDRA, PAPEL E TESOURA
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    Opições:                                                                                                                                                                                                                                                                                                              :)
    [ 1 ] - Pedra
    [ 2 ] - Papel
    [ 3 ] - Tesoura
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
''')
jogador = int(input('Digite uma das opições: '))
maquina = random.randint(1 , 3)

if jogador == 1 and maquina == 3  or jogador == 2 and maquina == 1 or jogador == 3 and maquina == 2 : 
    print('VOCÊ GANHOU!!!')

elif jogador == 3 and maquina == 1  or jogador == 1 and maquina == 2 or jogador == 2 and maquina == 3 :
    print('VOCÊ PERDEU!!')

elif jogador == 3 and maquina == 3  or jogador == 1 and maquina == 1 or jogador == 2 and maquina == 2 :
    print('O JOGO FICOU EMPATADO!!!')
