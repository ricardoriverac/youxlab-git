resposta = 'S'
pessoas = []
dados = []
numero = cadastro = 0
print('-'*50)
print('    PROGRAMA INICIADO    ')
print('-'*50)
while resposta == 'S':
    dados.append(str(input('-> ''Nome: ')))
    dados.append(float(input('-> ''Peso: ')))
    print('-'*50)
    resposta = str(input('-> ''Deseja continuar? [S/N]: ')).upper().strip()
    print('-'*50)
    if len(pessoas) == 0:
        numero = cadastro = dados[1]
    else:
        if dados[1] > numero:
            numero = dados[1]
        if dados[1] < cadastro:
            cadastro = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    if resposta in 'N':
        break
print('-'*50)
print('    PROGRAMA FINALIZADO     ')
print('-'*50)
print('-'f'Os cadastros informados foi {pessoas}')
print('-'f'Esse foi o tanto de pessoas cadastradas foi: {numero}.')
print('-'f'O maior peso que vc cadastrou foi: {numero} ', end='')
for i in pessoas:
    if i[1] == numero:
        print(f'[{i[0]}] ', end='')
print()
print('-'f'O menor peso cadastrado foi: {cadastro}', end='')
for i in pessoas:
    print(f'[{i[0]}]', end='')
    print()
    


    
