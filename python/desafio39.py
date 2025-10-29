from datetime import date
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.')
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE! ')
elif idade < 18:
    faltam = 18 - idade
    ano_alistamento = ano_atual + faltam
    print(f'Ainda faltam {faltam} anos para o alistamento.')
    print(f'Seu alistamento será em {ano_alistamento}.')
else:
    passou = idade - 18
    ano_alistamento = ano_atual - passou
    print(f'Você já deveria ter se alistado há {passou} anos.')
    print(f'Seu alistamento foi em {ano_alistamento}.')
