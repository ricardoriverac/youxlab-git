def leia_num(msg,tipo):
    if tipo == float:
        t = "real"
    elif tipo == int:
        t = "inteiro"
    while True:
        try:
            n = tipo(input(msg).replace(',','.'))
        except (ValueError,TypeError):
            print(f'\033[31m ERRO! Digite um numero {t} valido.\033[m')