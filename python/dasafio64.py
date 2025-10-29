n = int(input('Digite quantos termos da sequência de Fibonacci você quer ver: '))
t1, t2 = 0, 1
contador = 1
print('Sequência de Fibonacci:')
while contador <= n:
    print(t1, end=' → ')
    t1, t2 = t2, t1 + t2
    contador += 1
print('Fim')
