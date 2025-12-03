listaDnumeros = []
continuar = 'S'

while continuar == 'S':
    numero = int(input("Digite um número: "))
    if numero in listaDnumeros:
        while numero in listaDnumeros:
            numero = int(input("Esse número já foi adicionado. Adicione outro: "))
        listaDnumeros.append(numero)
    else:
        listaDnumeros.append(numero)
    print(listaDnumeros)
    continuar = str(input('Voce quer continuar [S/N]? ')).upper()     


for numero in sorted(listaDnumeros):
    print(f'{numero} -> ', end=' ') 
    