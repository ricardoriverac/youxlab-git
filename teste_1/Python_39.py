from datetime import date 
anoAtual = date.today().year
anodenascimento = int(input('Ano de nascimento:'))
idade = anoAtual - anodenascimento
print('Quem nasceu em {} tem {} anos em {}'.format(anodenascimento,idade,anoAtual))
if idade == 18:
        print('Você precisa se alistar imediatamente!')


elif idade < 18:
        conta =  18 - idade
        print('Atualmente você tem {} anos e falta {} anos para você se alistar'.format(idade,conta))

elif idade > 18: 
        conta2 = idade - 18
        print('Você deveria ter se alistado em {}anos atrás'.format(conta2))