# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
#  com quantos anos a pessoa vai se aposentar.

from datetime import datetime # 
pessoa=dict()

pessoa['nome']=str(input('Nome: '))
anoNascimento = int(input(f'Ano de nascimento de {pessoa["nome"]}: '))
pessoa['idade'] = datetime.now().year - anoNascimento
pessoa['carteira de trabalho']=int(input(f'Carteira de trabalho (0 não tem): '))

if pessoa['carteira de trabalho'] != 0:
    pessoa['ano de contratacao']=int(input(f'Ano de contratação: '))
    pessoa['salario']=float(input(f'Salário: R$ '))
    anosContribuicao = 35
    idadeAposentadoria = pessoa['idade'] + ((pessoa['ano de contratacao'] + anosContribuicao) - datetime.now().year)
    pessoa['idade aposentadoria'] = idadeAposentadoria
print('-='*50)
    
for k, v in pessoa.items():
    print(f'  - {k.title()}: {v}')
