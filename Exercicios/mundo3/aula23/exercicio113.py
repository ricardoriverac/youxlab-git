
def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except(ValueError, TypeError):
            print("Digite um número inteiro válido!")
            continue
        except KeyboardInterrupt:
            print("Finalizado!")
            return 0
        else:
            return numero
        

    
def leiaFloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except(ValueError, TypeError):
            print("Digite um número inteiro válido!")
            continue
        except KeyboardInterrupt:
            print("Finalizado!")
            return 0
        else:
            return numero

numInt = leiaInt("Digite um número inteiro: ")
numFloat = leiaFloat("Digite um número: ")


print(f'O valor inteiro digitado foi {numInt} e o valor float digitado foi {numFloat}')