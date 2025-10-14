from datetime import date
def ano(idade):
    if idade >= 70 or 16 <= idade < 18:
        print(f'Com {idade} anos, voto é opcional')
    elif idade <= 15:
        print(f'Com {idade} anos, voto não é obrigatório')
    else:
        print(f'Com {idade} anos, voto é obrigatório')


ano(date.today().year - int(input('Digite ano de nascimento: ')))