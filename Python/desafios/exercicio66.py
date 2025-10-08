n = s = 0
num_digitado = 0
while n != 999:
    num_digitado +=1
    n = int(input('Digite um numero: '))
    s += n
s -= 999
print(f'A soma dos{num_digitado}, é de {s}')