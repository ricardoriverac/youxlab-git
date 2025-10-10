pessoa = {}
galera = []
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break

media = soma / len(galera)
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('D) Lista das pessoas com idade acima da média:')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')