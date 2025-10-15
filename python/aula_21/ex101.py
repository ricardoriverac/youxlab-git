'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''


from datetime import date
def voto(nasc):
    atual = date.today().year
    idade = abs(nasc - atual)
    return idade


voto = voto(int(input('Em que ano você nasceu? ')))
if voto >= 65:
    print(f'Com {voto} anos: VOTO OPCIONAL.')
elif voto >= 18:
    print(f'Com {voto} anos: O VOTO É OBRIGATÓRIO.')
elif voto < 18:
    print(f'Com {voto} anos: NÃO VOTA.')