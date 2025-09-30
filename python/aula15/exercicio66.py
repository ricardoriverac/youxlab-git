qntd = count = soma = 0
while True:
    qntd = int(input('Digite um dígito qualquer: '))
    if qntd == 999:
        break
    else:
        print('>:(')
    count += 1 
    soma += qntd

print(f'{qntd} \n{soma}')