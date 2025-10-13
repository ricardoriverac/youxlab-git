numeros = []
maior = menor = 0
posicaoMaior = posicaoMenor = 0
count = 0

for cont in range(0, 6):
    numeros.append(int(input(f'Digite um número para a posição \033[33m{cont}\033[m: ')))

for posicao in range(len(numeros)):
    numeroPosicao = numeros[posicao]
    count +=1 

    if count == 1:
        maior = numeroPosicao
        menor = numeroPosicao

    if numeroPosicao > maior: 
        maior = numeroPosicao
        posicaoMaior = posicao

    if numeroPosicao < menor:
        menor = numeroPosicao
        posicaoMenor = posicao

print('-' * 55)
print(f'Os valores digitados por Você foram: {numeros}')
print(f'O maior número digitado foi o número \033[32m{max(numeros)}\033[m e ele está na \033[33m{posicaoMaior}\033[m posição.')
print(f'O menor número digitado foi o número \033[31m{min(numeros)}\033[m e ele está na \033[33m{posicaoMenor}\033[m posição.')