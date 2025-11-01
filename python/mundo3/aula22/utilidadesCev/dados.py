def leiaDinheiro(msg):
    while True:
        valor = input(msg)
        try:
            valor = float(valor)
            return valor
        except ValueError:
            print(f'ERRO: "{valor}" é um preço inválido!')