idade = 1
sexo = 'MF'
idadeCount = 1
masculino = 0
feminino = 0
maior = menor = 0
while True:
    idade = int(input(f'Digite a idade da {idadeCount}ª pessoa: '))
    if idade > 0:
        idadeCount += 1
    sexo = str(input('Digite qual o seu sexo: [M/F]  ')).upper()
    if sexo == 'M':
        masculino += 1
    if sexo == 'F':
        feminino += 1
    continuar = str(input('Deseja continuar? [S/N]  ')).upper()
    if continuar == 'N':
        break
    if idade >= 18:
        maior += 1
    if sexo == 'F':
        if idade < 20:
            feminino += 1

print(f'No total, há {maior} pessoas maiores que 18 anos.')
print(f'{masculino} Homens foram cadastrados.')
print(f'{feminino} Mulheres são menos que 20 anos.')