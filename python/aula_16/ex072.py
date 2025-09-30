'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
 de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis",
    "sete", "oito", "nove", "dez", "onze", "doze", "treze",
    "quatorze", "quinze", "dezesseis", "dezessete", "dezoito",
    "dezenove", "vinte"
)
digite_numero = int(input('Digite um número (entre 0 e 20): '))
while digite_numero < 0 or digite_numero >20:
    digite_numero = int(input('Digite um número (entre 0 e 20): '))

print(numeros_extenso[digite_numero])