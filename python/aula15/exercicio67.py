num = qntd = 0
while True:
    num = int(input('Digite o número escolhido: '))
    if num < 0:
        print('Não aceitamos números negativos, apenas números naturais.')
        break
    print('=-='*20)
    for c in range(1, 11):
        print(f'{num} * {c} = {num * c}')
    print('=-='*20)
    