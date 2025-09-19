numero=float(input('Digite um numero: '))
unidade=numero // 1 % 10
dezena=numero // 10 % 10
centena=numero // 100 % 10
milhar=numero // 1000 % 10
print(f'Seu numero é: {numero}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')