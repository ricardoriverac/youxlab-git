sexo = str(input('Informe seu sexo: [m/f] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Não entendemos, por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} informado, obrigado'.format(sexo))