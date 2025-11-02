def leiaInt(mensagem):
    ok = False
    valor = 0
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = int(input(numero))
            ok = True
        else: 
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return numero

numero = leiaInt(input('Digite um número:'))
print(f'Você acabou de digitar o número {numero}')