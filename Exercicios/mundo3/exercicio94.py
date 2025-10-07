galera = list()
pessoa = dict()
soma = média = 0

while True:
    pessoa.clear()
    pessoa ['nome'] = str(input('Nome: '))
    while True:
        pessoa ['sex'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa ['sex'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas Mou F.')
    pessoa ['idade'] = int(input('Idade: '))
    soma += pessoa ['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas Sou N.')
if resp 'N':
break

print(f'A) Ao todo temos (len(galera) pessoas cadastradas.')

média = soma / len(galera)

print(f'B) A média de idade é de (média: 5.2f) anos.')

print('C) As mulheres cadastradas foram', end='')