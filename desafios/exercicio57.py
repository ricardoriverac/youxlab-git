sexo = str(input('Digite qual o seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")