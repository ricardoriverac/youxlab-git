list = [[], []]
numd = []

for pi in range (1, 8):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        list[0].append(num)
    if num  % 2 == 1:
        list[1].append(num)
    numd.append(num)

print (f'os número digitados foram {numd}, os números pares são {list[0]}, e os impares são {list[1]}')