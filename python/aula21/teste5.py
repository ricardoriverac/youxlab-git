
def soma(a=0, b=0, c=0):
    '''
    retornando valores
    ao usar o comando return, você permite transportar um valor de uma variável local para fora de seu escopo
    segue o exemplo:
    '''    
    s = a+b+c
    return s

print(f'As somas foram: {soma(4, 5)} e {soma(3, 4, 5)}')
'''r1 = soma(3, 4, 5)
print(r1)
O valor de s foi retornado pela função e delcarado como valor da variável r1'''
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print('-'*30)
print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False
    
print('-' * 30)
v1 = int(input('Digite um valor: '))
if par(v1):
    print('-' * 30)
    print('É par!')
else:
    print('-'*30)
    print('É ímpar')