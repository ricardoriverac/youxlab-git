homens = 0
maiores18 = 0
totalmulher20 = 0
confirmar = 'S'
while confirmar in 'S':
    for pessoas in range(1, 999999999999):
        print(f'===== {pessoas}ª pessoa =====')
        nome = str(input('Nome: ')).strip()
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [M/F]: ')).strip()
        if idade >= 18:
            maiores18 += 1
        if sexo in 'Mm':
            homens += 1
        if sexo in 'Ff' and idade < 20:
            totalmulher20 =+ 1
        confirmar = str(input('deseja continuar?[S/N] ')).strip().upper()[0]
        if confirmar not in 'SN':
            confirmar = str(input('deseja continuar?[S/N] ')).strip().upper()[0]
        if confirmar in 'N':
            break
print(f'{maiores18} pessoas tem mais de 18 anos')
print(f'hà {homens} homems nesse grupo')
print(f'ao total {totalmulher20} mulheres tem menos de 20 anos')
