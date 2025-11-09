while True:
    
    sexo = str(input('Informe seu sexo: [M/F]:'))
    if sexo == 'M' or sexo == 'F':
        print('Sexo {} registrado com sucesso'.format(sexo))
        break

    else:
        print('Entrada inválida. Por favor, use apenas M ou F em letra maiúscula.')
        

