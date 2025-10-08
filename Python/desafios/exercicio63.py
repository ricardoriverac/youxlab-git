n_inteiros = str(input('Digite um numero inteiro qualquer: '))
def fibonacci_iterativo(n_termos):
    a, b = 0,1
    sequencia = []
    while len(sequencia) < n_termos:
        sequencia.append(a)
        a, b = b, a + b
    return sequencia
num_termos = 10
print(f'Sequência de fibonacci com {num_termos} termos (iterativo):')
print(fibonacci_iterativo(num_termos))