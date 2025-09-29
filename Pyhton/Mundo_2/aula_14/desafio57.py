sexo = str(input('Qual é o seu sexo? [feminino/masculino]'))
while sexo not in 'femininomasculino':
    sexo = str(input('Erro! digite de novo: [feminino/masculino]'))
print(f'Okay, sexo {sexo}, registrado!')