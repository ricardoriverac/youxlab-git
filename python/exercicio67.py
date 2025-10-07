num = int(input('digite um numero para ver sua tabuada '))
while num >= 0:
    for c in range(1, 11):
        print('{} x {:.2f} = {}'.format(c, num, c * num))
    num = int(input('digite um numero para ver sua tabuada '))
    