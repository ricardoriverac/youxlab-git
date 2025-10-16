print('-'*40)
print('       FUNÇÃO PARA FATORIAL:')
print()
def fatorial(num, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :parâmetro num: O número que vai ser fatorado.
    :parâmetro show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    ''' 
    fat = 1 #A variável fat vai guardar o resultado do fatorial.
            #Começa em 1, porque multiplicar por 1 não muda o valor.

    for cont in range(num, 0, -1): # Esse é um loop que começa no número escolhido (num) e vai até 1, contando de trás pra frente.

        if show: #O usuário quer ver a conta sendo mostrada?
                 #Se sim (show == True), entra nesse bloco.

            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= cont
    return fat

#PROGRAMA PRINCIPAL:
numDigitado = int(input('-- Digite um número parar fatorar: '))
print(fatorial(numDigitado, show=True))

# MANUAL: help(fatorial)
