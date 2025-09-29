import random
print ("This a game of 'Odd or Even'")
winner = 1
win = 0
while winner == 1:
    playerChoice = str(input('Odd [O] or Even [E]')).strip().upper()
    player = int(input('Choose a number: '))
    CPU = random.randint (1,10)
    sum = player + CPU
    if playerChoice == 'O':
        if sum % 2 == 1:
            print (f'You choose {player} and CPU choose {CPU}')
            print (f'You choose odds and you win')
            winner = 1
            win += 1
        else:
            print (f'You choose {player} and CPU choose {CPU}')
            print (f'You choose odds and you lose')
            break
    elif playerChoice == 'E':
        if sum % 2 == 0:
            print (f'You choose {player} and CPU choose {CPU}')
            print (f'You choose even and you win')
            winner = 1
            win += 1
        else:
            print (f'You choose {player} and CPU choose {CPU}')
            print (f'You choose even and you lose')
            break
print (f'You win {win} times!')