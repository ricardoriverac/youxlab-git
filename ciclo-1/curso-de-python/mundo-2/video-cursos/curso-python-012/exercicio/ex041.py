idade = int(input('Digite sua idade: '))

if idade <= 9:
    print('Você é considerado nadador Mirim.')

elif idade <= 14:
    print('Você é considerado nadador Infantil.')

elif idade <= 19:
    print('Você é considerado nadador Junior.')

elif idade == 20:
    print('Você é considerado nadador Sênior.')

elif idade > 20:
    print('Você é considerado nadador Master.')