idade = 0

idadeCount = 1
masculino = 0
feminino = 0
maior = menor = 0
while True:
    idade = int(input(f'Digite a idade da {idadeCount}ª pessoa: '))

    idadeCount += 1

    sexo = str(input('Digite qual o seu sexo: [M/F]  ')).upper()
    while True:
        if sexo == 'M':
            masculino += 1
            break
        elif sexo == 'F':
            feminino += 1
            break
        else:
            print("Inválido. Tente novamente.")
            sexo = str(input('Digite qual o seu sexo: [M/F]  ')).upper()

    continuar = str(input('Deseja continuar? [S/N]  ')).upper()
    if continuar == 'N':
        break

    if idade >= 18:
        maior += 1

    if sexo == 'F' and idade < 20:
        menor += 1


print(f'No total, há {maior} pessoas maiores que 18 anos.')
print(f'{masculino} Homens foram cadastrados.')
if menor <= 1:
    print(f'{menor} Apenas uma Mulher possui menos que 20 anos.')
elif menor >= 1:
    print(f'{menor} Mulheres são menos que 20 anos.')