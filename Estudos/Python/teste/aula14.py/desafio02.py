num= int(input('Informe o número: '))
u = num//1 % 10
d = num//10 %10
c = num //100 % 10
m= num// 1000 % 10
print(f'A unidade do número é {u}')
print(f'A dezena do número é {d}')
print(f'A centena do número é {c}')
print(f'O milhar do número é {m}')