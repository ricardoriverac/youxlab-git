import random

print('-' * 35)
print('PAR OU ÍMPAR')
print('-' * 35)

numero = 0
escolhaUsuario = 0
numeroAleatorio = 0
contagemDeVitoria = 0

while True:
    numero = int(input('Digite um número de 1 a 10: '))
    escolhaUsuario = str(input('Par ou Ímpar? [P/I]   ')).upper()
    numeroAleatorio = random.randint(1, 10)
    par = numero % 2 == 0
    impar = numero % 2 != 0

    if numero == par and escolhaUsuario == 'P' or numero == impar and escolhaUsuario == 'I':
        print(f'PARABÉNS!!! Você venceu!\nSeu número é {numero} e o meu é {numeroAleatorio}, a soma deles é igual a {numero + numeroAleatorio}')
        contagemDeVitoria += 1

    elif numero == par and escolhaUsuario == 'I' or numero == impar and escolhaUsuario == 'P':
        print('FIM DE JOGO! Você perdeu!')
        break

if contagemDeVitoria == 0:
    print(f'Você não teve nenhuma vitória.')

if contagemDeVitoria == 1:
    print(f'Você teve apenas 1 vitória consecutiva.')

if contagemDeVitoria > 1:
    print(f'Você teve {contagemDeVitoria} vitórias consecutivas.')