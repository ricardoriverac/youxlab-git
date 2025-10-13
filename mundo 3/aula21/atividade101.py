def voto(ano):
    from datetime import date 
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        print(f" com {idade} anos: VOTO NEGADO")
    elif 16 <= idade < 18 or idade >= 65:
        print(f"com {idade} anos: VOTO OPCIONAL")   
    else:
        print(f'com {idade} anos: VOTO OBRIGATORIO ')    
nascimento = int(input("ano de nascimneto: "))        
print(voto(nascimento))