valor_ser_sacado = int(input('Qual valor será sacado? R$'))
quantidade_Notas = 0
resto = 0

quantidade_Notas = valor_ser_sacado // 50
resto = valor_ser_sacado % 50
print(f'{quantidade_Notas} cédulas de R$50' )
quantidade_Notas = resto // 20
resto = resto % 20
print(f'{quantidade_Notas} cédulas de R$20')
quantidade_Notas = resto // 10
resto = resto % 10
print(f'{quantidade_Notas} cédulas de R$10')
quantidade_Notas = resto // 1
resto = resto % 1
print(f'{quantidade_Notas} cédulas de R$1')