numero=float(input('Digite um numero: '))
u=numero // 1 % 10
d=numero // 10 % 10
c=numero // 100 % 10
m=numero // 1000 % 10
print(f'Seu numero é: {numero}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')