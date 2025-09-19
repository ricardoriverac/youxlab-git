# testes aula 10

nome = str(input('Qual é o seu nome?'))
if nome == 'Marcela':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
    print(f'Bom dia,{nome}')

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
média = (nota_1 + nota_2)/2
print(f'A sua média foi {média}')
if média>=6.0 :
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!!!')

# CONDIÇÕES SIMPLIFICADAS
print('PARABÉNS!' if média>=6 else 'ESTUDE MAIS!')
