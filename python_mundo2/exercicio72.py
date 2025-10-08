nu = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove'
      , 'dez', 'onze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito'
      , 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número: '))
    if 0 < num < 20 :
        break 
    print ('Você digitou um número invalido')
print (f'O número que você digitou é {nu[num]}')