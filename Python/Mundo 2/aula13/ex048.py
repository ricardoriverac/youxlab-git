soma = 0
for c in range(0, 500, 3):
    if (c %2) != 0: # != >>> diferente de
        print(c)
        soma += c 
print(f'O somátorio de todos os valores foi {soma}')
