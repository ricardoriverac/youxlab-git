soma = 0
menor = 0
count = 0
maisVelho = 0
nomeMaisVelho = ''

for c in range(1,5):
    nome = str(input(f'Digite o nome da {c}ª pessoa: ')).upper()
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {c}ª pessoa: ')).upper()
    count += 1

    soma += idade

    if count == 1:
        maisVelho = idade
        nomeMaisVelho = nome
    else:
        if idade > maisVelho and sexo == 'M':
            maisVelho = idade
            nomeMaisVelho = nome

    if sexo == 'F' and idade < 20:
        menor += 1

print(f'\nA média de idade do grupo é de {soma / c:.0f}.')
print(f'O homem mais velho do grupo é o {nomeMaisVelho}.')

if menor == 1:
    print(f'Apenas 1 mulher do grupo possuir menos que 20 anos.')
if menor > 1:
    print(f'{menor} mulheres são menores que 20 anos.')