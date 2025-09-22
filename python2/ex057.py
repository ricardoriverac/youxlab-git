sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos,por favor digite novamente: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso')