s = str(input('Qual o seu sexo [M]asculino ou [F]eminino ')).strip().upper()
while s[0] not in 'MF':
    s = str(input(f'Entrada {s} inválida, por favor digite novamente: ')).strip().upper()
print('Sexo masculino registrado!' if s[0] == 'M' else 'Sexo feminino registrado!')
