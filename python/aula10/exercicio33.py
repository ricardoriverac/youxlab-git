a = int(input('Valor 1: '))
b = int(input('Valor 2: '))
c = int(input('Valor 3: '))
#verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > b and c>a:
    maior = c 
print(f'O menor valor é {menor} e o maior valor é {maior}')
