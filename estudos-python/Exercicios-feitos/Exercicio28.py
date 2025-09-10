import random
import emoji
randomNumber = random.randint (0,5)
selectedNumber = int(input('Enter a number between 0 and 5 - '))
if randomNumber == selectedNumber:
    print ('Parabéns você acertou✅')
else:
    print ('Você errou❌')