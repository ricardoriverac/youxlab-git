#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date
def voto(nasci):
    ano_atual = date.today().year
    idade = ano_atual - nasci
    if idade < 16:
        return f'Com {idade} anos:NÃO VOTA.'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos:VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos:VOTO OBRIGATÓRIO.'
ano_str = input('Em que ano você nasceu: ')
ano_int = int(ano_str)
result = voto(ano_int)
print(result)