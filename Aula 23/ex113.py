def leiaInt(msg): 
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro: Digite um número inteiro válido.\033[m')
        except(KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n
 

numero1 = leiaInt('Digite um INTEIRO:' )
numero2 = leiaFloat('Digite um REAL:')
print(f'O valor INTEIRO digitado foi {numero1} e o REAL foi {numero2}')
