from datetime import date
dic = {'nome': str(input('Nome: ')),
       'ano de nascimento': int(input('Ano de nascimento: ')),
       'carteira de Trabalho': int(input('CTPS: [0 se não possuir] '))}
dic['idade'] = date.today().year - dic['ano de nascimento']
if dic['carteira de Trabalho'] != 0:
    dic['anoDeContratacao'] = int(input('Ano de contratação: '))
    dic['salario'] = float(input('Salário: R$'))
dic['aposentadoria'] = 60 - dic['idade']
print(dic)
print(f'idade: {dic["idade"]} \naposentadoria: {dic["aposentadoria"]}')