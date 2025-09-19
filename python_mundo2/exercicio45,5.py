import random
print ('[1] pedra')
print ('[2] papel')
print ('[3] tesoura')
opj = int(input('ecolha uma opção: '))
opc = [1, 2, 3]
esc = random.choice(opc)
if opj == 1:
    if esc == 3 :
        print ('Você ganhou, a opção da maquina foi tesoura')
        print (esc)
    elif esc == 1:
        print ('Você empatou, a opção da maquina foi pedra')
        print (esc)
    elif esc == 2:
        print ('Você perdeu, a opção da maquina foi papel')
        print (esc)
elif opj == 2:
    if esc == 1:
        print ('Você ganhou, a opção da maquina foi pedra')
        print(esc)
    elif esc == 3:
        print ('Você perdeu, a opção da maquina foi tesoura')
        print(esc)
    elif esc == 2 :
        print ('Você empatou, a opção da maquina foi papel')
        print(esc)
elif opj == 3: 
    if esc == 2 :
        print ('Você ganhou, a opção da maquina foi papel')
    elif esc == 1:
        print ('Você perdeu, a opção da maquina foi pedra')
    elif esc == 3:
        print ('Você empatou, a opção da maquina foi tesoura')