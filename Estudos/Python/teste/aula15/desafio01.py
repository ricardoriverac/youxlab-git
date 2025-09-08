import random
import emoji
numeroEscolhido=int(input('Tente acertar o número que o computador está pensando: '))
sorteio= random.choice([1, 2, 3, 4, 5])
if numeroEscolhido==sorteio:
    print('Você acertou!!')
else:
    print(emoji.emojize('Você errou!! Seu burro :rolling_on_the_floor_laughing:'))