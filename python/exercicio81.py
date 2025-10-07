listaNumero = []
resposta = 'S'
while resposta == 'S':
    numero = int(input(f'digite o valor: '))
    resposta = str(input(f'deseja continuar? [S/N]: ')).upper( )
    listaNumero.append(numero)

print()
print(f'o valor 5 aparece {(listaNumero.count(5))} vezes na lista')
print(f'os numeros decrescente sao {listaNumero}')
