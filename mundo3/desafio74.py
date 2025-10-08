from random import randint

num1 = randint(1, 10)
num2 = randint(1, 10)
num3 = randint(1, 10)
num4 = randint(1, 10)
num5 = randint(1, 10)

tuple = (num1, num2, num3, num4, num5)

print(f'Os valores sorteados foram: {tuple}')
print(f'O maior valor sorteado foi {max(tuple)}')
print(f'O menor valor sorteado foi {min(tuple)}')