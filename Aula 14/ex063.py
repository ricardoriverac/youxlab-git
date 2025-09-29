print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
numero_termos = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print('~'*30)
print('{} -> {}'.format(termo1, termo2), end='')
cont = 3
while cont <= numero_termos:
    termo3 = termo1 + termo2
    print('-> {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(' -> FIM!')
print('~'*30)