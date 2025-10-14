galera = list()
dado = list()
totalmaioridade = 0
totalmenoridade = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmaioridade = totalmaioridade + 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenoridade = totalmenoridade + 1
print(f'temos{totalmaioridade} maiores e {totalmenoridade} menores de idade.')