sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'Mmf':
    sexo = str('Dados inválidos. Por favor,informe seu sexo:').strip().upper()[0]
print('Sexo {} registrado com sucesso'.fotmat(sexo))