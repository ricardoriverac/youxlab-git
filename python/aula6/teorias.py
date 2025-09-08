n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))
s = n1 + n2
print('A soma entre {} e {} vale: {}'.format(n1,n2,s))

n1 = int(input('Digite um valor: '))
print(type(n1))

n1 = str(input('Digite algo: '))
print(type(n1))
print(n1.isnumeric())
print(n1.isalnum())
print(n1.isalpha())