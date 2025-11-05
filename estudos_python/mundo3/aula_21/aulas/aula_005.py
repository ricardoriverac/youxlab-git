def div(n1, n2):
    '''
    Funcionalidade: Ele serve para dividir 2 números.
    Para funcionar e necessario colocar dois números
    dentro dos parenteses
    '''
    r = n1 / n2
    return r

n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
divisão = div(n1, n2)
print(f'O resultado resultado da divisão e {divisão}')

