# Tupla com os números por extenso de 0 a 20
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros[num]}.')
    else:
        print('Número fora do intervalo. Tente novamente.')
        continue

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break

print('Programa encerrado. Volte sempre!')
