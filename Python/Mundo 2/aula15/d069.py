resposta = 's'
contadorMais18 = 0 
contadorHomens = 0
contadorMulheres20 = 0 
while resposta == 's':
    idade = int(input('Sua idade: '))
    sexo = str(input('Seu sexo [f/m]: '))
    if idade > 18:
        contadorMais18 += 1
    if sexo == 'm':
        contadorHomens += 1
    else:
        if idade > 20:
            contadorMulheres20 += 1
    resposta = str(input('Você deseja continuar? [s/n]: '))
print(f'Foram cadastradas {contadorMais18} pessoas MAIORES 18 anos.\nForam cadastrados {contadorHomens} HOMENS.\nForam cadastradas {contadorMulheres20} mulheres MAIORES de 20 anos.')
print('='*40)
print('CADASTRO ENCERRADO')
print('='*40)