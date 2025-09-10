Ano = int(input('Digite um ano: '))
bissexto = Ano % 4
print(bissexto)
if bissexto == 0:
    print(f'{Ano} é um ano BISSEXTO!')
else:
    print(f'{Ano} não é um ano BISSEXTO!')
