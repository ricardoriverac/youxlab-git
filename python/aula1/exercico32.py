from datetime import date
ano=int(input("Qual ano voce quer analisar? Coloque 0 para analisar o ano atual: "))
if ano % 4 == 0:
    ano=date.today().year
    print(f"O ano {ano} é BISSEXTO")
else:
    print(f'O ano {ano} não e BISSEXTO')
    