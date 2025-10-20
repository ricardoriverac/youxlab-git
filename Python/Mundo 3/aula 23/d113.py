print('-'*60)

def leiaint(msg):
    while True: #Ficar lendo até a pessoa digitar um número certo.
        try:
            n = int(input(msg))
        except (ValueError, TypeError): #Se for erro de valor ou erro de tipo
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue #Isso faz voltar para o começo do while, e fazendo o usuário tentar novamente.
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True: #Ficar lendo até a pessoa digitar um número certo.
        try:
            n = float(input(msg))
        except (ValueError, TypeError): #Se for erro de valor ou erro de tipo
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue #Isso faz voltar para o começo do while, e fazendo o usuário tentar novamente.
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


numero1 = leiaint('Digite um número INTEIRO: ')
numero2 = leiafloat('Digite um número REAL: ')
print(f'O valor INTEIRO foi: {numero1} e o REAL foi: {numero2}')
print('-'*60)
