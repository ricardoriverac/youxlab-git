from datetime import date
ano_atual=date.today().year
print(ano_atual)
ano_de_nascimento=int(input('Qual a data do seu nascimento?: '))
idade=ano_atual - ano_de_nascimento

if idade<=9:
    print("MINRIM")
elif idade<=14:
    print("INFANTIL")
elif idade<=19:
    print("JUNIOR")
elif idade<=20:
    print("SỄNIOR")
else:
    print("MASTER")