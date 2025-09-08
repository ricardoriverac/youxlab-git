tempo=int(input('Quanto tempo tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

nome = str(input('Qual o seu nome? ')).upper()
print('Belo nome' if nome == 'RODINEI' else 'nome feio')