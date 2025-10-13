dados = {}
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
print (f'O nome é igual a {dados["nome"]}')
print (f'A média é igual a {dados["media"]}')
if dados['media'] >= 6:
    print (f'Situação é aprovado')
else:
    print (f'Situação é reprovado')