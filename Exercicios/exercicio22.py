nome=str(input('Digite seu nome completo: '))
espaco=nome.replace("","")
num_letras=len(espaco)
primeiro_nome=nome.split()[0]
quantidade_letras=len(primeiro_nome.replace('',''))
print(nome.upper())
print(nome.lower())
print(f'O numero de letras no nome é: {num_letras}')
print(f'A quantidade de letras do primeiro nome é: {quantidade_letras}')