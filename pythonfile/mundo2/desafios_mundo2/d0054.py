from datetime import date
anoatual = date.today().year
maior =  0
for c in range(0,7):
   idade = date.today().year - int(input('Digite seu ano de nascimento: '))
   if idade  >= 18:
    maior += 1
print(f'Entre essas 7 pessoas existem {maior} maior de idade e {7 - maior} menores de idade')