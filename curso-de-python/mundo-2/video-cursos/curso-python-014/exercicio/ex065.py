valor = 0
soma = 0
maior = menor = 0
count = 1
continuar = ''
while True:
    valor = int(input(f'Digite o {count}º número: '))
    soma += valor
    count += 1

    if count == 2:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    continuar = str(input('Você quer continuar? [S/N]  ')).upper()
    if continuar == 'N':
        break

    if continuar != 'S':
        print('\033[31mInválido. Tente novamente.')
        while True:
            continuar = str(input('\033[mVocê quer continuar? [S/N]  ')).upper()
            if continuar == 'S':
                break

print(f'A \033[33mmédia\033[m entre todos os números é {soma / (count - 1):.0f}')
print(f'O \033[32mmaior\033[m número lido é {maior}')
print(f'O \033[31mmenor\033[m número lido é {menor}')