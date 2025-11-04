from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - ano_nasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - date.today().year)
print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k.capitalize()}: {v}')
