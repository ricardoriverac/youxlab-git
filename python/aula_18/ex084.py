'''
 Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

pessoa = []
comeco = []
numero = cadastro = 0
while True:
    pessoa.append(str(input('digite o nome que vc deseja cadastrar: ')))
    pessoa.append(float(input('Digite o peso da pessoa cadastrada: ')))
    if len(comeco) == 0:
        numero = cadastro = pessoa[1]
    else:
        if pessoa[1] > numero:
            numero = pessoa[1]
        if pessoa[1] < cadastro:
            cadastro = pessoa[1]
    comeco.append(pessoa[:])
    pessoa.clear()
    certo = str(input('Dseja continuar? [S/N] '))
    if certo in 'Nn':
        break
print('=' * 50)
print('Os cadastros informados foi {}'.format(comeco))
print(f'Esse foi o tanto de pessoas cadastradas foi: {numero}.')
print(f'O maior peso que vc cadastrou foi: {numero} ', end='')
for i in comeco:
    if i[1] == numero:
        print(f'[{i[0]}] ', end='')
print()
print(f'O menor peso cadastrado foi: {cadastro}', end='')
for i in comeco:
    print(f'[{i[0]}]', end='')
    print()