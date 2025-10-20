def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
        return f
    def dobra(n):
        return n * 2
    def triplo(n):
        return n * 3
    
num = int(input('digite um valor: '))
fat = fatorial(num)
print(f'o fatorial de {num} e {fat}.')

