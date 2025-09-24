count = 0
countF = 0
homem = 0
soma = 0
media = 0 
nomeVelho = ''
for c in range(1, 5):
    print('-'*4, f'{c} PESSOA', '-'*4)
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    soma += idade
    count += 1 
    if sexo in 'F' and idade <= 20:
        countF += 1
    elif sexo in 'F' and countF == 0:
        countF == 'Não há mulheres'
    elif c == 1 and sexo in 'M':
        sexo = homem
        if idade > homem:
            homem = idade
            nomeVelho = nome
media = (soma)/count
print(f'A média é {media}')
print(f'{nomeVelho}')
print(f'{countF}')