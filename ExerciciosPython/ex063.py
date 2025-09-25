n = int(input('Digite um número: '))
a = 0
b = 1
contagem = 0 
while contagem < n:
    print(a, end=' ')
    proximo = a + b
    a = b
    b = proximo
    contagem += 1 