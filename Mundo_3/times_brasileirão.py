times = ('Atletico Mineiro', 'Flamengo' , 'Palmeiras' , 'Cruzeiro' ,
         'Botafogo' , 'São Paulo' , 'Bahia' , 'Vasco' , 'Fluminense',
         'Corinthians' , 'Internacional' , 'Sport' , 'Vitoria' ,
         'Mirassol' , 'Gremio' , 'Ceara' , 'Bragrantino' ,
         'Santos' , 'Juventude' , 'Fortaleza')
print('-=' * 15)
print(f'Lista de times do Brasileirão 2025: {times}')
print('-= * 15')
print(f'Os 5 primeiros times são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos times são {times[-4:]}')
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O Gremio esta na {times.index("Gremio")+1}° posição')