print('~'*30)
print('Iremos falar sobre a sequência de fibonacci')
print('-'*50)
numero = int(input('Quantos termos vc quer mostrar? '))
numero1= 0
numero2 = 1
print('-'*30)
print('{} - {}'.format(numero1, numero2), end='')
conta = 3
sequencia = " "
while conta <= numero:
    numero3 = numero1 + numero2
    sequencia += " " + str(numero3)
    numero1 = numero2
    numero2 = numero3
    conta += 1
print(' -> fim')
print(f'{sequencia}')
