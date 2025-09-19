nome = str(input('Qual è seu nome? '))
if nome == 'Isabela':
    print('Que nome lindo você tem!')
else: 
    print('Seu nome é tão normal!')
print('Bom dia {}!'.format(nome))






numero1 = float(input('Digite a primeira nota: '))
numero2 = float(input('Digite a segunda nota: '))
media = (numero1 + numero2)/2
print('A média foi {:.1f}'.format(media))
if media >= 6.0:
    print('Sua média foi muitooo boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
    