from datetime import date
ano_atual=date.today().year
print(ano_atual)
nascimento=int(input('Qual a data do seu nascimento?: '))
idade= ano_atual - nascimento

if idade<18:
    print("Você ainda vai se alistar!")
elif idade==18:
    print("Você ja pode se alistar!")
else:
    print("Já passou do tempo de alistamento!")