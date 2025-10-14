def voto():
    idade = int(input('Ano de nascimento: '))
    votoo = 2025 - idade
    if votoo >= 18:
        print (f'O seu voto é obrigatorio')
    elif votoo >= 16:
        print (f'O seu voto é opcional ')
    elif votoo <=15:
        print (f'O seu voto foi negado')

voto()