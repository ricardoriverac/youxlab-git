#importações
import random 
#entradas, ontantes e variaveis  
numero=int(input('Estou pensando em um numero '))
computador=random.randint(0,10)
valor=int(1)
#processamento
while numero!=computador:
    if numero>computador:
        print('Mais...Tente novamente ')
    else:
        print('Menos...Tente novamente ')
    numero=int(input('Estou pensando em um numero '))
    valor=valor+1     
print(f'Você acertou!')
print(f'Você tentou {valor} vezes.Parabens')