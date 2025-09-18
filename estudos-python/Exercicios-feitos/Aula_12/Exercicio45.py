import random
#1- paper 2- rock 3-rock
yourChoice = int(input('Make a choice:\n1-paper\n2-rock\n3-scissors\nYour choice is: '))
machineChoice = random.randint(1,3)
if yourChoice == 1 and machineChoice == 1 or yourChoice == 2 and machineChoice == 2 or yourChoice == 3 and machineChoice == 3:
    print ('It is a tie!!!')
elif yourChoice == 1 and machineChoice == 2 or yourChoice == 2 and machineChoice == 3 or yourChoice == 3 and machineChoice == 1:
    print ('You win!!!')
elif machineChoice == 1 and yourChoice == 2 or machineChoice == 2 and yourChoice == 3 or machineChoice == 3 and yourChoice == 1:
    print ('You lose!!!')