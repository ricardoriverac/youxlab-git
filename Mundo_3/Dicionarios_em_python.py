temp = {}
temp['nome'] = str(input('Digite o Nome: ')).strip().title()
temp['media'] = int(input('Digite a média: '))
if temp['media'] >= 7:
    temp['situação'] = 'Aprovado'
elif 5 < temp['media'] < 7:
    temp['situação'] = 'Recuperação'
else:
    temp['situação'] = 'Reprovado'
print(temp)
for k, v in temp.items():
    print(f'O {k} é igual a {v}')