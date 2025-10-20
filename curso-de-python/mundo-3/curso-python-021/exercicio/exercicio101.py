def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade < 16:
        return (f'com {idade} ano: NAO VOTA')
    elif 16 <= idade < 18 or idade > 70:
        return (f'com {idade} anos: VOTO OPCIONAL')
    else:
        return (f'com {idade} anos: VOTO OBRIGATORIO')

print(voto(2009))
    
