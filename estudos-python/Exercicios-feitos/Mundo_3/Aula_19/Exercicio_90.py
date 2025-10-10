info = {}
lista = []
quantidade = int(input('Quantos alunos você quer avaliar?'))
for c in range (quantidade):
    info['nome'] = (str(input('Nome:')))
    media = (float(input('Média:')))
    info['media'] = (media)
    if media <= 5.9:
        info['situacao'] = ('Reprovado')
    else:
        info['situacao'] = ('Passou')
    lista.append(info.copy())
for p in lista:
    for k, v in p.items():
        print(f'{k} = {v}')