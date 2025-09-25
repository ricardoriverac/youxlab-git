sexo = str(input('Qual seu sexo? [M/F]: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))
print(f'Sexo {sexo} definido.')