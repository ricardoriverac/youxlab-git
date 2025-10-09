dados= list()
bancoDados= list()
listaMaior = list()
listaMenor = list()
continuacao= 'dsada'
maior = 0
menor = 9999
while continuacao not in 'N':
    nome= (str(input('Cadastre o nome da pessoa: ')))
    idade= (int(input(f'Cadastre o peso de {dados}')))
    dados.append(nome)
    dados.append(idade)
    bancoDados.append(dados[:])
    for nome in dados:
        if idade > maior:
            maior= idade
        if idade < menor:
            menor= idade
    dados.clear()
    continuacao= str(input('Deseja continuar? [S/N]'))
print(f'Ao todo você cadastrou {len(bancoDados[0])} pessoas')
print(f'O maior peso foi  {maior}. Peso de {nome}')
print(f'O menor peso foi {menor}. Peso de {nome} ')