sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while sexo not in ['M', 'F']:
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo corretamente [M/F]: ')).strip().upper()

print(f'Sexo {sexo} registrado com sucesso!')
