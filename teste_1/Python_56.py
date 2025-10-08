somaIdade = 0
menoresDe20 = 0
maisVelhoNome = ''
maisVelhoIdade = 0 

import statistics 
for p in range(1,5):
    print('-----{} PESSOA ------'.format(p))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('[M/F]:')).strip().upper()

    somaIdade += idade


    # Verifica a pessoa mais velha até agora 
    if idade > maisVelhoIdade:
        maisVelhoIdade = idade
        maisVelhoNome = nome

    # Conta as mulheres com menos de 20 anos 
    if sexo == 'F' and idade < 20:
        menoresDe20 +=1

    # Calcula média de idade 
    mediaDeIdade = somaIdade / 4


else:   
    print('A média de idade é {:.1f} anos '.format(mediaDeIdade))
    print('A pessoa mais velha tem {} anos e se chama {}'.format(maisVelhoIdade,maisVelhoNome))
    print('Ao todo são {} homem(ns) com menos de 20 anos'.format(menoresDe20))