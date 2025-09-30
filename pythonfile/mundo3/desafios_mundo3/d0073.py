times = ('flamengo', 'cruzeiro', 'palmeiras', 'botafogo', 'bahia', 'são paulo', 'fluminense',
        'gremio', 'ceara', 'vasco', 'corinthians', 'santos', 'fortaleza', 'internacional', 'Chapeconhense',
            'mirassol', 'vitoria', 'bragantino', 'botafogo', 'atletico-mg')

for cont in range(0, len(times)):
    print(f'Os 5 primeiros times são {times[:5]}')

for ultimos in range(0, len(times)):
    print(f'\nOs 4 ultimos times são {times[16:]}')

    timesOrdem = sorted(times)
    for c in timesOrdem:
        print(f'Ordem alfabetica: {c}')

    for index,d in enumerate(times):
        if (times[index] == 'Chapeconhense'):
            print(f'A posiçpão do chapecoense esta em {index +1}')