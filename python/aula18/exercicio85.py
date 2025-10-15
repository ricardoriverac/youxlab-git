lista = [[], []]
maior = menor = num = 0
for c in range(1,8):
    num = int(input(f'Digite o valor {c}: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'{lista[0]}')
print(f'{lista[1]}')