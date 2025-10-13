def leiaint(msg):
    while True:
        entrada = input(msg)
        if entrada.isnumeric():
            return int(entrada)
        else:
            print("digite um numero inteiro valido")
numero = leiaint("digite um numero: ") 
print(f"voce digitou o numero {numero}")          

