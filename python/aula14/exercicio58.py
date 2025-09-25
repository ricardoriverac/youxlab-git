from random import randint
computador = randint(0,10)
count = 0
acertou = False
while not acertou:
    pessoa = int(input('Digite um número qualquer, entre 0 e 10, e tente acertar!  '))
    count +=1
    if pessoa ==  computador:
        acertou = True
    else:
        if pessoa < computador:
            print('Mais... tente novamente!')
        elif pessoa > computador:
            print('Menos... tente novamente!')
print(f'Acertou!!!!!!!!!!!\n', '-=-'*8, f'\nO número era {computador} \nVocê teve {count} tentativas até acertar!\n', '-=-'*8)
