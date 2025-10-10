from datetime import date
ano_atual=date.today().year
print(ano_atual)
nascimento=int(input('Qual o ano do seu nascimento?: '))
idade= ano_atual - nascimento
anos_passados=idade - 18

if idade<18:
    print("Você ainda vai se alistar!")
elif idade==18:
    print("Você ja pode se alistar!")
else:
    print("Já passou do tempo de alistamento!")
    print(f"Já se passaram {anos_passados} anos que voce não pode mais se alistar!")