homens = 0
mulheres = 0
somaIdade = 0
maisVelho = 0
mulheresMaisNovas = 0 
nomeHomemMaisVelho = ''
for pessoa in range(1, 5):
    nome = input('Insira o nome da pessoa: ')
    idade = int(input('Insira a idade da pessoa: '))
    sexo = input('Você é homem ou mulher:\nInsira H para homem ou M para mulher: ').strip().upper()
    somaIdade += idade
    print(f'O nome da pessoa é {nome}')
    print(f'A idade dessa pessoa é {idade}')
    print(f'O sexo dessa pessoa é {sexo}')
    if sexo == 'M':
        mulheres += 1
        if idade<20:
            mulheresMaisNovas += 1
    if sexo == 'H':
        homens += 1
        if idade>maisVelho:
            maisVelho == idade
            nomeHomemMaisVelho = nome
media = float(somaIdade/4)
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho é {nomeHomemMaisVelho}.')
print(f'Tem {mulheresMaisNovas} menores de 20 anos.')