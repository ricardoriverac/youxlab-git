resp = 'S'
cadastro = {}
dados = []
anoAtual = 2025
print('-'*35)
print('     CADASTRE SEUS DADOS     ')
print('-'*35)
while resp == 'S':
    dados.append(str(input('-> Nome: ')))
    dados.append(int(input('-> Ano de Nascimento: ')))
    idade = anoAtual - dados[1]
    dados.append(int(input('-> CTPS (0 se n possuir): ')))
    cadastro['Nome'] = (dados[0])
    cadastro['CTPS'] = (dados[2])
    cadastro['Ano de Nascimento'] = (dados[1])
    cadastro['Idade'] = (idade)
    if dados[2] != 0:
        cadastro['Contratação'] = int(input('-> Ano de contratação: '))
        cadastro['Salário'] = float(input('-> Salário: '))
        cadastro['Aposentadoria'] = cadastro["Contratação"] + 35
        cadastro['Aposentadoria'] = cadastro["Aposentadoria"] - cadastro["Ano de Nascimento"]
        print('=-'*17)
        print('  ->->->-> DADOS FINAIS <-<-<-<-')
        print('=-'*17)
        print(f'-Nome: {cadastro["Nome"]}.\n-Idade: {cadastro["Idade"]}.\n-CTPS (Carteira de Trabalho): {cadastro["CTPS"]}.\n-Salário: {cadastro["Salário"]}\n-Você aposentará com {cadastro["Aposentadoria"]}.')
        print('-'*35)
        print('FINALIZANDO...')
        break
        if dados[2] == 0:
            print('=-'*17)
            print('  ->->->-> DADOS FINAIS <-<-<-<-')
            print('=-'*17)
            print('-'*35)
            print('FINALIZANDO...')
            break
    else:
        print(f'-Trabalhador(a): {cadastro["Nome"]}.\n-Idade: {cadastro["Idade"]} anos.\n-Carteira de Trabalho: {cadastro["CTPS"]}.')
        print('FINALIZANDO...')
        break
print('-'*35)


