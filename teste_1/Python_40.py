primeiranota = float(input('Primeira nota: ')) 
segundanota = float(input('Segunta nota: '))
media = (primeiranota + segundanota) / 2
if 10 > media >= 7:
    print('A primeira nota do aluno e {} a segunda e {} a média total do aluno será de {}'.format(primeiranota,segundanota,media))
    print('O aluno foi APROVADO')
elif 7 > media >= 5:
    print('A primeira nota do aluno e {} a segunda e {} a média total do aluno será de {}'.format(primeiranota,segundanota,media))
    print('O aluno ficou de RECUPERAÇÃO')
elif 5 > media >= 0:
    print('A primeira nota do aluno e {} a segunda e {} a média total do aluno será de {}'.format(primeiranota,segundanota,media))
    print('O aluno foi REPROVADO')
else:
    print('ERRO!!!, Digite um número entre 0 a 10!!')