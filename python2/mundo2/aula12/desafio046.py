import random
player= str(input('Pedra, Papel ou Tesoura? '))
cpu = random.choice(['Pedra', 'Papel', 'Tesoura'])

#Combinações com Tesoura e geral
if cpu == 'Pedra' and player== 'Tesoura':
    print(str('Cpu venceu! '))
elif cpu== 'Tesoura' and player== 'Pedra':
    print(str('Player venceu! '))
elif cpu== 'Tesoura' and player== 'Papel':
    print(str('cpu venceu! '))
elif cpu== 'Papel' and player== 'Tesoura':
    print(str('Player venceu! '))

 #Combinações com Pedra e papel
    if cpu == 'Pedra' and player== 'Papel':
        print(str('Player venceu! '))
    elif cpu== 'Papel' and player== 'Pedra':
        print(str('Cpu venceu! '))
    else:
        print(str('Empate! '))