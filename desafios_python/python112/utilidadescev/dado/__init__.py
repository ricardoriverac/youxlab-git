def leiaDinheiro(mensagem):
    valida = False
    while not valida:
        entrada = str(input(mensagem)).replace(',','.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)

def leiaint(mensagem):
    ok = False
    valor = 0 
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válida.\033[m')
        if ok: 
            break
    return valor
        
