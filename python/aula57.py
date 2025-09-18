sexo = str(input('informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados invalidos. por favor, informe seu sexo: '))
print('sexo {} regitrado com sucesso'.format(sexo))