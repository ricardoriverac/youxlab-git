from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Informe o ano que você nasceu: '))
    idade = date.today().year - ano
    if idade < 21 :
        menor += 1
    else:
        maior +=1
print('{} ainda não atingiram a maioridade e {} já são maiores.'.format(menor, maior))