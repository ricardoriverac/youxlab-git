# idade = int(input('Digite sua idade: '))
# sexo = str(input('Digite  qual é o seu sexo: ')).upper
continuar = 'S'
pessoas = 0 
homens = 0
mulheres = 0
total = 0 
while continuar not in 'N':
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite  qual é o seu sexo [F/M]: ')).upper()
    while sexo not in 'FM':
        print('ERRO,digite novamente ')
        sexo = str(input('Digite  qual é o seu sexo [F/M]: ')).upper()
    else:
        if idade >= 18:
            pessoas += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade <20:
            mulheres += 1
        total += 1    
    continuar = str(input('Voce quer continuar?[S/N]')).upper()
print(f'No total {pessoas} pessoas adultas foram registradas\n foram um total de {homens} homens registrados\n e {mulheres} sao mulheres com menos de 20 anos')