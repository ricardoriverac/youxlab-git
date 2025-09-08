numero=float(input('Digite um numero: '))
unidade=numero // 1 % 10
dezena=numero // 10 % 10
centena=numero // 100 % 10
mmilhar=numero // 1000 % 10
print(f'Seu numero é: {numero}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')