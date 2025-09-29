print('Gerador de PA')
print('--' * 10)
primeiro = int(input('Primeiro: '))
razao = int(input('Razão da PA: '))
termo = primeiro
conta = 1
tudo = 0
repor = 10
while repor != 0:
    tudo = tudo + repor
    while conta <= tudo:
        print('{} __ '.format(termo), end='')
        termo += razao
        conta += 1
    print('pare')
    repor = int(input('Até quantos termos você quer apresentar? '))
print('Acabamos por aqui, agradeço sua paciência')
print(f'A progressão foi concluída com {tudo} termos apresentados.')