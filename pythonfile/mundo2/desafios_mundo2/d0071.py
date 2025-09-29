cedula1 = 0
cedula10 = 0
cedula20 = 0
cedula50 = 0
resto = 0

caixa = int(input('Quantos você quer sacar?: '))

cedula50 = caixa // 50
resto = caixa % 50


cedula20 = resto // 20
resto = caixa % 20


cedula10 = resto // 10
resto = caixa % 10


cedula1 = resto // 1

print(f'Você sacou {cedula50} cedulas de 50, {cedula20} cedulas de 20, {cedula10} cedulas de 10 e {cedula1} cedulas de 1.')
