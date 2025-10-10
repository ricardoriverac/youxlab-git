from datetime import date
ano_atual=date.today().year
print(ano_atual)
contador_maiores = 0
contador_menores = 0

for idade in range(7):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {idade+1}ª pessoa: "))
    idade = ano_atual- ano_nascimento
    if idade >= 18:
        contador_maiores += 1 
    else:
        contador_menores += 1  
print(f"\nDas 7 pessoas, {contador_maiores} são maiores de idade.")
print(f"E {contador_menores} pessoas ainda não atingiram a maioridade.")