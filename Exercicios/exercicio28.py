import random
computador=random.randint(0,5)
pessoa=int(input('Digite um numero e veja se vocễ venceu ou perdeu: '))

if pessoa==computador:
    print('Voce venceu')
else:
    print('Voce perdeu')
print(f"O numero do computador é: {computador}")