# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(msg):

    aceito = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():# ele vai indicar se verdade ou mentira
            valor = int(n)
            aceito = True
        else:
            print('digite um numero inteiro valido')
        if aceito:
            break
    return valor
n = leiaInt('digite um numero: ')
print(f'voce acabou de digitar o numero: {n}')