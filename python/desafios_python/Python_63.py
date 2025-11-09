print('-=' * 13)
print('Sequência de Fibonacci')
print('-='* 13)
termos = int(input('Quantos termos você quer mostrar?:'))
numero1 = 0
numero2 = 1
print('-=' * 13)
print('{} -> {}'.format(numero1,numero2), end='')
while termos > 1:
    numero3 = numero1 + numero2
    numero1 = numero2
    numero2 = numero3 
    print('-> {}'.format(numero3), end='')
    termos -= 1
