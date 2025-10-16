def leiaInt(msg):

    while True:

        try:
            n = int(input(msg))
            return n
        except (ValueError):
            print('ERROR! Digite um número inteiro valido.')
        except KeyboardInterrupt:
            print('\nUsuário interrompeu a entrada de dados.')
            return 0
    
def leiaFloat(dgt):

    while True:

        try:
            n = float(input(dgt))
            return n
        except (ValueError):   
            print('ERROR! Digite um número real valido.')
        except KeyboardInterrupt:
            print('\nUsuário interrompeu a entrada de dados.')
            return 0.0       
                
inteiro = leiaInt("Digite um número inteiro: ")
real = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {inteiro} e o real {real}.')