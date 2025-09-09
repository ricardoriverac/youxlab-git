import calendar
ano=int(input('Digite um ano: '))

if calendar.isleap(ano):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")