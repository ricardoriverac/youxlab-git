from pickle import TRUE

cont =('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True: # type: ignore
    numero =int(input('um numero de 0 a 20: '))
    if numero > 20:
            print('menor que 20 jão')
            break
    else:
        print(f'voce digitou o numero {cont[numero]}')

