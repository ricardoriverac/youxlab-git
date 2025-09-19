print('ALISTAMENTO MILITAR\nDigite os seus dados no formulário abaixo:')
ano = int(input('Em que ano você nasceu: '))
idade = 2025 - ano
print(f'Sua idade é {idade}')
if idade < 18:
    anos = 18 - idade
    print(f'Você ainda é de menor volte para a escola!\nVocê só poderá se alistar daqui a {anos} anos.')
elif idade == 18:
    print(f'Você já pode se alistar, pois já tem {idade}.')
elif idade > 18:
    anos2 = idade - 18
    print(f'Você já deveria ter se alisatado a {anos2} anos!')