import random
computador=random.randint(0,10)
pessoa=int(input('Digite um numero e veja se vocẽ venceu ou perdeu: '))
chutes= 1

while pessoa != computador:
    print('Você errrou')
    pessoa=int(input("Digite outro numero: "))
    chutes += 1
print(f"Você ganhou em {chutes} jogadas!")