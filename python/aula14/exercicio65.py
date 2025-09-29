soma = qntd = media = maior = menor = 0
escolha = 'S'
while escolha in 'Ss':
    numEscolhido = int(input('Digtite qualquer número: '))
    escolha = str(input('Você quer continuar?  [S/N]\n')).strip().upper()[0]
    qntd += 1
    soma += numEscolhido
    media = soma/qntd
    if qntd == 1:
        maior = menor = numEscolhido
    else:
        if numEscolhido > maior:
            maior = numEscolhido
        if numEscolhido < menor:
            menor = numEscolhido
print('=-='*20)
print(f'quantidade de números: {qntd} \nmédia: {media} \nmaior: {maior} \nmenor: {menor}')
print('=-='*20)