'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano 
de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

#Resposta

from datetime import date
data_atual = date.today() 
ano_atual = data_atual.year


def voto():

    if ano_atual - ano_nascimento >= 18:
        print('Voto OBRIGATORIO!!!')

    elif ano_atual - ano_nascimento < 18 and ano_atual - ano_nascimento >= 16:
        print('Voto OPCIONAL!!!')

    elif ano_atual - ano_nascimento < 16:
        print('Voto NEGADO!!!')

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
print(f'A idade da pessoa e {ano_atual - ano_nascimento}: {voto()}')
