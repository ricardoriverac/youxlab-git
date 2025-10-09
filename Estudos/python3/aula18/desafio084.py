dados= list()
bancoDados= list()
listaMaior = list()
nome=list()
NomeMaior= list()
nomeMenor=list()
listaMenor = list()
pessoas=list()  
continuacao= 'S'
maior = 0
menor = 9999
while continuacao not in 'N':
    nome.append((str(input('Cadastre o nome da pessoa: '))))
    dados.append(nome[:])
    peso= (float(input(f'Cadastre o peso de {dados}')))
    dados.append(peso)
    bancoDados.append(dados[:])
    if peso > maior:
        maior= peso
        NomeMaior.clear()
        NomeMaior.append(nome[:])
    elif peso == maior:
        NomeMaior.append(nome[:])
    if peso < menor:
        nomeMenor.clear()
        nomeMenor.append(nome[:])
        menor= peso
    elif peso == menor:
        nomeMenor.append(nome[:])
    nome.clear()
    dados.clear()
    continuacao= str(input('Deseja continuar? [S/N]'))
print(f'Ao todo você cadastrou {len(bancoDados[0])} pessoas')
print(f'O maior peso foi  {maior}. Peso de {NomeMaior}')
print(f'O menor peso foi {menor}. Peso de {nomeMenor}')