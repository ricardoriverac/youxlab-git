sexo = str(input('insira seu sexo ')).upper()
while sexo != 'M' and 'N':
    novosexo = str(input('dado inválido,por favor insira seu sexo ')).upper()
    sexo = novosexo
print(f'seu sexo foi cadastrado como {sexo}')