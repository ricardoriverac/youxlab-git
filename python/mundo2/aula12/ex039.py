#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a
# sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.

import datetime
ano_atual = datetime.date.today( ).year
nasci = int(input('Informe em qual ano você nasceu: '))
idade = ano_atual - nasci
if idade < 18:
    ano_falta = 18 - idade
    print(f'Você tem {idade} anos, falta {ano_falta} ano para voê se alistar.')
elif idade == 18:
    print(f'Você tem {idade} anos, está na hora de se alistar.')
else:
    anos_passa = idade - 18
    print(f'Você tem {idade} anos, já se passaram {anos_passa} ano que você podia ter se alistado.')


