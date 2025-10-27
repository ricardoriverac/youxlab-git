from datetime import date
while True:
    nome = str(input('Digite seu nome:')).title()
    idade = int(input('Digite sua idade:'))
    nota = float(input('Digite uma nota (Entre 0 e 10):'))
    
    if nota < 0 or nota > 10:
        print('ERRO!! SÓ ACEITAMOS NÚMEROS ENTRE 0 E 10!\nTente novamente...\n')

    else:
     break

if nota >= 7.0:
    situacao = ('Acima da média da turma')
else:
    situacao = ('Abaixo da média da turma')


print(f'\nSeu nome e {nome}')
print(f'Você tem {idade} de idade')


if idade >= 100:
    print('Você já tem 100 anos Parabéns! Me conte o segredo')

else:
     conta = 100 - idade
     print(f'Faltam {conta} anos para você fazer 100 anos')

print(f'Sua nota foi {nota}')
print(f'Situação: {situacao}')

   