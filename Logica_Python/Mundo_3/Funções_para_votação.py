def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: NÃO PODE VOTAR!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: O VOTO É OBRIGATÓRIO!'
    


nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))