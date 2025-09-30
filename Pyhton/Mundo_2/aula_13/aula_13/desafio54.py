from datetime import date
anoatual = date.today().year
maiortotal = 0
menortotal = 0
for c in range(0,7):
    anonascimento = int(input('Digite o ano de nascimento: '))
    idade = anoatual - anonascimento
    if idade >=21:
        maiortotal +=1
    else:
        menortotal +=1
print(f'No total temos {maiortotal} pessoas maiores de idade e {menortotal} pessoas menores de idade.')
