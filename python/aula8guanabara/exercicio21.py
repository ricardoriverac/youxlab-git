num = int(input('Digite qualquer número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'{u} \n{d} \n{c} \n{m}')