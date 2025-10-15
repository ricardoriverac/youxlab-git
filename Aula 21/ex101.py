from datetime import date
def voto(nasc):
    atual = date.today().year
    idade = abs(nasc - atual)
    return idade


voto = voto(int(input('Em que ano você nasceu? ')))
if voto >= 65:
    print(f'Tendo {voto} anos: VOTO OPCIONAL.')
elif voto >= 18:
    print(f'Tendo {voto} anos: O VOTO É OBRIGATÓRIO.')
elif voto < 18:
    print(f'Tendo {voto} anos: NÃO VOTA.')