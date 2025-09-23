import random
adivinhar= int(input('Adivinhe o que o computador está pensando: '))
computador= random.randint(0, 10)
tentativa=1
while adivinhar != (computador):
    if adivinhar < computador:
        print(str(f'Mais... tente novamente! {tentativa} tentativa'))
        
    else:
        print(str(f'Menos... tente novamente! {tentativa} tentativa'))
    adivinhar=int(input('Adivinhe o que o computador está pensando: '))
    tentativa+=1
print(f'Parabéns! Você acertou com {tentativa} tentativas!!')
    