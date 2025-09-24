from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
atual = 2025
if (atual - ano >= 18) and (atual - ano <= 19):
    print('Chegou a hora de se alistar no exército.')
    print('O Dia da Defesa Nacional pode ocorrer entre \033[30;107m14 de janeiro e 21 de novembro\033[m.')
    print('Se faz anos depois desta data então o seu alistamento acontecerá no próximo ano.')
elif atual - ano < 18:
    print('Ainda não chegou a altura de se alistar no exército.')
    print(f'Ainda falta/m \033[32m{18 - (atual - ano)}\033[m anos')
    print(f'O seu ano de alistamento será em \033[32m{(18 -(atual-ano)) + ano}\033[m.')
elif atual - ano > 19:
    print('Já passou da altura de se alistar no exército.')
    print(f'Já passou/passaram \033[1;31m{(atual - ano) - 18}\033[m anos.')
    print(f'Seu alistamento foi em \033[1;31m{atual - ((atual - ano) - 18)}\033[m.')