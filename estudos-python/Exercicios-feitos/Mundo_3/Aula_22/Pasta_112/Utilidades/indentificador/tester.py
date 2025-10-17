def readNumber(character):
    valid = False
    while not valid:
        entrada = str(character).replace(',','.')
        if entrada.isalpha() or entrada == '':
            print(f'Falha {entrada} Preço inválido!')
        elif entrada.isnumeric():
            valid = True
            return float(entrada)