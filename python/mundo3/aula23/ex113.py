#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
# digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
# com a mesma funcionalidade.

def leiaInt(num='Digite um número:'):
    while True:
        try:
            entrada = input('Digite um número inteiro:')
            valor = int(entrada)
            return valor
        except ValueError:
            print('\033[1;31mERRO, digite o número inteiro corretamente\033[0m')
valor_rece = leiaInt()
print(f'O número recebido foi:{valor_rece}')

def leiaFloat(num='Digite um número real:'):
    while True:
        try:
            entra = input('Digite um número real:')
            valor = float(entra)
            return valor
        except ValueError:
            print('\033[1;31mErro, digite um número real corretamente\033[0m')
valor_recebido = leiaFloat()
print(f'O valor real recebido foi:{valor_recebido}')
