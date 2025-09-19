pessoas= int(input('Quantas pessoas vão participar da análise? ').replace('pessoas', ''))
somaPessoas=0
somaIdade=0
Idademaior=0
IdadeMenor= 18
countMulheres=0

for c in range (1, pessoas+1):
    # media=0
    # IdadeMenor
    # idadeMaior=0
    # countMulheres=0
    somaPessoas+=1
    nome= str(input(f'Qual nome da {somaPessoas}ª pessoa? '))
    idade= int(input(f'Qual idade da {somaPessoas}ª pessoa? '))
    sexualidade= str(input(f'Qual a sexualidade da {somaPessoas}ª pessoa? [M ou F]').upper().strip())
    
    somaIdade= somaIdade+idade
    print(str(f'-------- {somaPessoas}ª pessoa--------'))
    print(f'NOME: {nome}')
    print(f'IDADE: {idade}')
    print(f'SEXUALIDADE: {sexualidade}')

    if sexualidade == 'M':
        if idade> Idademaior:
            Idademaior=idade
            HomemmaisVelho= nome
    if sexualidade == 'F':
        if idade < IdadeMenor:
            countMulheres= countMulheres+1

print(f'O homem mais velho tem {Idademaior} anos e se chama {HomemmaisVelho}')
print(f'Ao todo temos {countMulheres} mulheres menores de idade.')
mediaIdade_final= somaIdade/somaPessoas
print(f'A media de idade do grupo é {mediaIdade_final}')
