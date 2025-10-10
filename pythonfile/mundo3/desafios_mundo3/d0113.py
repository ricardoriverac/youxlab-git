def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))            
        except (ValueError, TypeError):
            print('ERRO, Digite um numero inteiro.')
            continue
        except (KeyboardInterrupt):
            print('O usuario preferiu não digitar esse numero')
            return 0
        else:
            return valor

def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO, Digite um numero real.')
            continue
        except (KeyboardInterrupt):
            print('O usuario preferiu não digitar esse numero.')
            return 0
        else:
            return valor


numero = leiaint('Digite um numero Inteiro: ')
print(f'Voce digitou o numero -> {numero}')
numero_float = leiafloat('Digite um numero Real: ')
print(f'Você digitou o numero -> {numero_float}')