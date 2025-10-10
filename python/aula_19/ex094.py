'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
'''

numero1 = list()
numero2 = dict()
certo = média = 0
while True:
    numero2.clear()
    numero2['nome'] = str(input('Nome: '))
    while True:
        numero2['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if numero2['sexo'] in 'MF':
            break
        print('Nosso programa nn entendeu, por favor digite se seu sexo é M ou F.')
    numero2['idade'] = int(input('Digite sua idade por favor: '))
    certo += numero2['idade']
    numero1.append(numero2.copy())
    while True: 
        i = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if i in 'SN':
            break
        print('Nosso programa não entendeu, por favor informe apenas com S ou N.')
    if i == 'N':
       break
print('=' * 50)
print(f'A) Esse é o total de pessoas cadastradas: {len(numero1)}')
média = certo / len(numero2)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) O total de mulheres cadastradas foram: ', end='')
for n in numero1:
    if n['sexo'] in 'Ff':
        print(f'{n["nome"]} ', end='')
print()
print('D) Esse é total de pessoas acima da média: ')
for n in numero1:
    if n['idade'] >= média:
        print('      ', end='')
        for k, v in n.items():
            print(f'{k} = {v}; ', end='')
print('Obrigado por colaborar, agradeço ')