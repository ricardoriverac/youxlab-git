'''
Crie um programa onde ele diz se o número é par ou impar
'''
def par_impar(numero):
    if numero % 2 == 0:
        print(f'{numero} - Par')
    else:
        print(f'{numero} - Impar')

par_impar(int(input('par_impar: ')))


