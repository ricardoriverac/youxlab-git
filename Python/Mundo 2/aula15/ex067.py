print('TABUADA 3.0')
while True:
    tabuada = int(input('Digite um valor para saber a tabuada: '))
    print('-' * 30)
    for contador in range(1, 11):
        print(f'{tabuada} x {contador} = {tabuada * contador}')
        print('-' * 30)
    if tabuada < 0:
        break
print('Tabuada encerrada!')