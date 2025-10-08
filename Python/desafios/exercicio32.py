import calendar
anoBi = int(input('Digite um ano qualquer: '))
if calendar.isleap(anoBi):
    print (f'O ano de {anoBi}, é um ano bisesto')
else:
    print(f'O ano de {anoBi} não é um ano bisesto')