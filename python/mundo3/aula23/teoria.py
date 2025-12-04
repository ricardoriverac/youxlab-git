#Teoria aula23.
try:
    num1 = int(input('Digite um número:'))
    num2 = int(input('Digite o segundo número:'))
    multi = num1 * num2
except:
    print('ERRO, certifique se digitou o número corretamente!!')
else:
    print(f'O resultado da multiplicação é:{multi}')
finally:
    print('Tenha uma boa tarde, volte sempre!!')