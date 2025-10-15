def leitorInteiro(p):
    while True:
        a= str(input(p))
        if a.isdigit():
            return a
        else:
            print(f'ERRO! DIGITE UM NUMERO INTEIRO VÁLIDO! ')
n= leitorInteiro('Digite um número: ')
print(f'Você acabou de digitar {n} ')
