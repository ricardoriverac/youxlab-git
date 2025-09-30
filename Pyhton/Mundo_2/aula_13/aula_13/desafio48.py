conta = 0
for c in range(0, 501, 3):
    print(c)
    if c % 3 == 0:
        conta = conta + c
print(f'o resultado da conta é {conta}')