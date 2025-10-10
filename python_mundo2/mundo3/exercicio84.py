temp = []
perm = []
menor = 0 
maior = 0
peso = 0
count = 0

while True :
    temp.append(str(input('Qual seu nome? ')))
    temp.append(float(input('Qual seu peso? Kg ')))
    if len(perm) == 0 :
        maior = temp[1]
        menor = temp[1]
    if maior < temp[1]:
        maior = temp [1]
    elif menor > temp[1]:
        menor = temp[1]
    perm.append(temp[:])
    temp.clear()
    
    while True:
        c = str(input('Você quer continuar? [S/N]: ')).upper()
        if c == 'S':
            break
        if c == 'N':
            break
        else:
            print ('você não digitou nenhuma das alternativas, digite novamente')
    if c == 'N':
        break
for p in perm :
    if p[1] == maior:
        print (f'A pessoa com o maior peso é {p[0]}')
for d in perm:
    if d[1] == menor:
        print (f'o menor peso foi do {d[0]}')
print (f'os dados são {perm}, você cadastrou {len(perm)} pessoas, o menor peso é de {menor}, e o maior é {maior}')