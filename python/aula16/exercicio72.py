c = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    resp = int(input('Digite um número entre 0 e 20: '))
    if 0<= resp <= 20:
        break
    print('tente novamente')
print(f'você digitou {c[resp]}')