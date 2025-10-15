def leitorInteiro(p):
    """leitorInteiro(p)
       -> Valida se a entrada é numeral ou não, caso não seja será retornado uma solicitação para digitar um numero
       :param p: Reconhece a mensagem digitada"""
    while True:
        a= str(input(p))
        if a.isdigit():
            return a
        else:
            print(f'ERRO! DIGITE UM NUMERO INTEIRO VÁLIDO! ')
n= leitorInteiro('Digite um número: ')
print(f'Você acabou de digitar {n} ')
