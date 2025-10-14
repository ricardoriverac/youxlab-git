listaPessoas=list()
pessoa=list()
pessoasLeves=list()
pessoasPesadas=list()
resposta='S'

while resposta != 'N':
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    listaPessoas.append(pessoa.copy())
    pessoa.clear()
    resposta=str(input('Quer continuar? S/N ')).upper()

for p in listaPessoas:
    if p[1] >= 100:
        pessoasPesadas.append(p)
    elif p[1] <=70:
        pessoasLeves.append(p)
        
print(f'A quantidade de pessoas cadastradas foram {len(listaPessoas)}')
print(f'A lista das pessoas mais pesadas é {pessoasPesadas}')
print(f'A lista de pessas mais leves é {pessoasLeves}')        
        