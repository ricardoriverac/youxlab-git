nome = str(input('Qual é o seu nome? '))
if nome == 'Agatha': 
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é tao normal')
print(f'Bom dia {nome}!')    

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua media foi {m}')
if m >= 6.0:
    print('Sua media foi boa! PARABENS!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')   