from time import sleep
contagem1 = 1
contagem2 = 10
print('1 até 10 de 1 em 1:')
while contagem1 < 11:
    print(contagem1)
    contagem1 += 1
print('10 até 0 de 2 em 2')
while contagem2 > -1:
    print(contagem2)
    contagem2 -= 2
print('Personalize sua pŕopria sequência:')
def contador(a, b, c):
    while a != b:
        print(a, end=' ')
        a += c
contador(a=int(input('Insira o número inicial: ')), b=int(input('Insira o número final: ')), c=int(input('Insira o número e a passagem: ')))
