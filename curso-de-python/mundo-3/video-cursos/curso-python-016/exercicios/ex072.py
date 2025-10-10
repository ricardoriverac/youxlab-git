numeroExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

for resposta in numeroExtenso:
    numero = int(input('Digite um númer de 1 a 20: '))
    print(f'Você digitou o número {numeroExtenso[numero]}.')
    break