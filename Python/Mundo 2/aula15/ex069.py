contadorMaioridade = 0
contadorHomens = 0
contadorMulheres20anos = 0
continuar = 's'
while continuar == 's':
    sexo = str(input('Digite o seu sexo: [F/M] ')).upper()
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Letra inválida, digite as letras a seguir novamente até acerta-las [F/M] ')).upper()
    idade = int(input('Digite a sua idade: '))
    if idade >= 18:
        contadorMaioridade += 1 
    if sexo == 'M':
        contadorHomens += 1
    else:
        if idade <= 20:
            contadorMulheres20anos += 1
    continuar = str(input('Deseja continuar? [S/N]: '))
print(f'{contadorMaioridade} pessoas tem mais de 18 anos.')
print(f'{contadorMulheres20anos} mulheres tem menos de 20 anos.')
print(f'{contadorHomens} homens foram cadastrados. ')
    