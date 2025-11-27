#Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico
# (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(num=5, show=True):
    fatori = 1
    for c in range(num, 0, -1):
        fatori *= c
    return fatori
print(f'O fatorial de "5" é: {fatorial(5)}.')


