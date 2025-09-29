tabuada = int(input('Digite um número para obter sua tabuada: '))
while tabuada > 0:
    for tabuada2 in range(1, 11):
        print(f'{tabuada} x {tabuada2} = {tabuada * tabuada2}')
    tabuada = int(input('Digite outro número para obter sua tabuada [Digite um número negativo para parar]: '))
    if tabuada <= 0:
        print('=' * 10, 'PROGRAMA INTERROMPIDO!', '=' * 10)
