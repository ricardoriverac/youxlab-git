print('Gerador de PA')
print('-=' * 10)
contador = 0

primeiroTermo = int(input('Primeiro Termo:'))
razao = int(input('Razão da PA:'))
termo = primeiroTermo
conta = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while conta <= total:
        print('{} ->'.format(termo),end='')
        termo += razao
        conta += 1 
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
