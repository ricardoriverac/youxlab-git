# condição simples
nome = str(input('Qual é o seu nome? '))
if nome == 'Ana Laura':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}!'.format(nome))

# condições
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Qual a segunda nota: '))
media = (nota1 + nota2)/2 
print('A sua media foi {:.1f}'.format(media))
if media >= 6.0:
    print('Sua media foi boa! PARABÉNS!')
else: 
    print('Sua media foi ruim! ESTUDE MAIS!')