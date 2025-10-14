def leiaint(mensagem):
    
    while True:
        numero = input(mensagem)
        if numero.isnumeric():
            return int(numero)
        print('isso não é um valor inteiro.')
    
numero = leiaint('Digite um valor: ')
print(f'Numero digitado: {numero}')