print('_'*30)
print('sequencia de fibonacci')
print('_'*30)
n = int(input('quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
cont = 0
print('~'*30)
print(' {}  {}'.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' {}'.format(t1, t2), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM')
print('~'*30)
