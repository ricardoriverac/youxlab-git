def voto(ano_nascimento):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano_nascimento
    
    if idade < 16:
        return f'Com {idade}, voto negado!'
    elif idade == 16 and 18:
        return f'Com {idade}, é opciona o seu voto!'
    else:
        return f'Com {idade}, é obrigatorio seu voto!'
    
funcao = voto(2007)
print(funcao)