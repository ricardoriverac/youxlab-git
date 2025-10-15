def votos(vt):
    calculo= 2025 - nascimento
    if calculo < 16:
        print(f'Com {calculo} anos: SEM PERMISSÃO PARA VOTO')
    elif calculo >= 16 and calculo < 18:
        print(f'Com {calculo} anos: VOTO OPCIONAL')
    else:
        print(f'com {calculo} anos: VOTO OBRIGATORIO')



nascimento=int(input('Em qual ano você nasceu? '))
votos(nascimento)