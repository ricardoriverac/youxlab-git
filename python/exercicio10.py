#converter um número em metro para cm e milímetros

num = float(input())
metro = str(num) + 'm'
centi = str(num * 100) + 'cm'
mili = str(num * 1000) + 'mm'

print('O número {0} em metros é igual a {1}, em cm é igual a {2} e em milímetros é {3}.'.format(num, metro, centi, mili))