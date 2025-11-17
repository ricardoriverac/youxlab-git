sexo = 'MF' 
continuar = 'S'

while continuar != 'N' and continuar == 'S':
    resposta = str(input('Qual seu sexo? [M/F]  ')).upper()
    if resposta not in sexo:
        print('Resposta Inválida! Responda com "M" ou "F"')

    else:
        print(f'O seu sexo é {resposta}')
        print('Resposta Válida.')
    continuar = str(input('Quer continuar? [S/N]  ')).upper()

print('Programa encerrado.')