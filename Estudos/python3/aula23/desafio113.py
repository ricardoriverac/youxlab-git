def leaint(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (TypeError, ValueError):
            print("Digite um número inteiro válido!!")
            continue

        except (KeyboardInterrupt):
            print("O usuário prefiriu não digitar nada! Programa encerrado!")
            return 0
        else:
            return numero

def leiaFloat(msg):
    while True:
        try:
            number=float(input(msg))
        except (TypeError, ValueError):
            print("Digite um número real válido!! ")
            continue
        except(KeyboardInterrupt):
            print("O usuario preferiu não digitar nada!")
            return 0
        else: 
            return number
    
    







numeroInt = leaint("Digite um número inteiro: ")
numeroFloat= leiaFloat("Digite um número real")
print(f'O numero inteiro digitado foi {numeroInt} o numero real digitado foi {numeroFloat}')