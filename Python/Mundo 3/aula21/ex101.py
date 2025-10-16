# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL e OBRIGATÓRIO nas eleições.]

def voto(anoNascimento):
    from datetime import date
    anoAtual=date.today().year
    idade = anoAtual - anoNascimento
    if idade < 16:
        return f'Você tem {idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade <65:
        return f'Você tem {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Você tem {idade} anos: VOTO OBRIGATÓRIO.'
print(voto(2009))