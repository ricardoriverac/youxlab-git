countIdade=0
countHomens=0
countMulheres=0
continuação='dsad'
while continuação not in 'N':
    print('CADASTRE UMA PESSOA')
    idade= int(input('Qual a idade da pessoa? '))
    if idade > 18:
        countIdade=countIdade+1
    sexo= str(input('Qual o sexo da pessoa? [F/M]')).upper()
    if sexo == 'M':
        countHomens=countHomens+1
    if sexo == 'F' and idade < 20:
        countMulheres=countMulheres+1
    continuação= str(input('Você quer continuar? [S/N]')).upper()
print(f'Total de pessoas com mais de 18 anos: {countIdade}')
print(f'Total de homens cadastrados é: {countHomens}')
print(f'Total de mulheres com menos de 20 anos é: {countMulheres}')