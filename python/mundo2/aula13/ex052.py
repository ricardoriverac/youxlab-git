# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

import math

def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
numero = int(input("Digite um número inteiro para verificar se é primo: "))
if is_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")