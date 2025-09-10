tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
 print('carro novo')
else:
 print('carro velho')
print('--FIM--') 

nome = str(input('Qual é o seu nome? '))
if nome == 'Luis':
 print('Que nome lindo você tem!')
else:
 print('Seu nome é normal!')
print('Bom dia {}!'.format(nome))

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS!' if m >=6 else 'ESTUDE MAIS!')
