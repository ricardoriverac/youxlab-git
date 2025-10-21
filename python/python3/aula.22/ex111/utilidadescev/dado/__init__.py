def leiadinheiro(txt):
    valido = False
    while not valido:
        entrada = str(input(txt)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO {txt} preco invalido')
        else:
            valido = True
            return float(entrada)


    