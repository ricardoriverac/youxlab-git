import random
print ('''escolha uma opção
       [1] pedra
       [2] papel
       [3] tesoura''')
opj = int(input('Qual opção você deseja? '))                            #opção do jogador
opc = [1, 2, 3]                                      #opção do computador
escolhido = random.choice(opc)
if opj == 1 and escolhido == 3 :
    print ('ganhou PARABÉNS!!a opção do computador era {}'.format(pedra))
elif opj == 2 and escolhido == 1 :
    print ('ganhou PARABÉNS!!a opção do computador era {}'.format(papel))
elif opj == 3 and escolhido == 2 :
    print ('ganhou PARABÉNS!!a opção do computador era {}'.format(tesoura))
elif opj == opc:
    print('você empatou com a maquina')