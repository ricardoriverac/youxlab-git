def voto(anoDeNascimento):
    
    idade=2025-anoDeNascimento
    
    if idade >= 16 and idade <=17:
        return print(f'Você tem {idade} anos.Pode escolhar se vai votar ou não ')
    elif idade < 16:
        return f'Você tem {idade} anos.Voto negado'
    elif idade > 17 and idade < 70:
        return f'Você tem {idade} anos.Voto obrigatorio'
    elif idade > 69:
        return f'Você esta com {idade} anos,esta a cima da media.Voto opcional'

anoDeNascimento=int(input('Que ano você nasceu? '))

voto(anoDeNascimento)