quantidadeNotas = 0
valorSacar = int(input('Qual valor será sacado? R$'))
resto = 0

quantidadeNotas = valorSacar // 50
resto = valorSacar % 50
print(f'{quantidadeNotas} cédulas de R$50' )
quantidadeNotas = resto // 20
resto = resto % 20
print(f'{quantidadeNotas} cédulas de R$20')
quantidadeNotas = resto // 10
resto = resto % 10
print(f'{quantidadeNotas} cédulas de R$10')
quantidadeNotas = resto // 1
resto = resto % 1
print(f'{quantidadeNotas} cédulas de R$1')