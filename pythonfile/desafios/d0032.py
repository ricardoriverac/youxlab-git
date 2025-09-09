import calendar
ano = int(input('Digite um ano: '))
if calendar.isleap(ano):
    print(f' {ano} É um ano bissexto. ')
else:
    print(f'{ano} Não é um ano bissexto. ')