from datetime import date
anoatual = date.today().year
maiores =  0
for c in range(0,7):
   idade = date.today().year - int(input('Digite seu ano de nascimento: '))
   if idade  >= 18:
    maiores += 1
print(f'Entre essas 7 pessoas existem {maiores} maiores de idade e {7 - maiores} menores de idade')