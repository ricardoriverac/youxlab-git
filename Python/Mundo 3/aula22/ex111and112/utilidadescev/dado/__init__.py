def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\33[0;31mERRO:\"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True 
            return float(entrada)
        
def leiaInt(msg):

    aceito = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():# ele vai indicar se verdade ou mentira
            valor = int(n)
            aceito = True
        else:
            print('\033[0;31mERROR! Digite um número inteiro válido.\033[m')
        if aceito:
            break
    return valor