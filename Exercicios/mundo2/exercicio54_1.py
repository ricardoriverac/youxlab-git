#anos de nascimento
from datetime import date
ano_atual=date.today().year
print(ano_atual)
pessoa1=float(input('Digite o ano do nascimento: '))
pessoa2=float(input('Digite o ano do nascimento: '))
pessoa3=float(input('Digite o ano do nascimento: '))
pessoa4=float(input('Digite o ano do nascimento: '))
pessoa5=float(input('Digite o ano do nascimento: '))
pessoa6=float(input('Digite o ano do nascimento: '))
pessoa7=float(input('Digite o ano do nascimento: '))
pessoas=[pessoa1, pessoa2, pessoa3, pessoa4, pessoa5, pessoa6, pessoa7]

contador_maior=0
contador_menor=0

for ano_de_nascimento in pessoas:
    if (ano_atual - ano_de_nascimento) >= 18:
        contador_maior += 1
        # contador_maior = contador_maior +1
    else:  
        contador_menor += 1

print(f"Ha {contador_maior} pessoas maior de idade!")
print(f" Ha {contador_menor} pessoas menores de idade!")
    