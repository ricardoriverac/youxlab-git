'''
Crie um programa que tenha uma dupla totalmente preenchida com uma 
contagem por extenso, de zero até vinte. Seu programa deverá ler 
um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

#Resposta

numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
    "dezoito", "dezenove", "vinte"
)

while True:
    numero = int(input('Digite o número que deseja ver por extenso[0 a 20]: '))

    if numero > 20:
        numero = int(input('Número invalido. Escolha algum número de 0 a 20: '))

    break

print(f'O número {numero} por extenso e {numeros_extenso[numero]}.')