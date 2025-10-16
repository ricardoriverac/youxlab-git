valores = [int(input(f'Digite o {n+1}º valor: ')) for n in range(9)]

matriz = [valores[0:3], valores[3:6], valores[6:9]]


for linha in matriz:
    for numero in linha:
        print(f'[ {numero:^5} ]', end='')
    print()

soma_pares = sum(numero for linha in matriz for numero in linha if numero % 2 == 0)
soma_coluna3 = sum(linha[2] for linha in matriz)
maior_segunda = max(matriz[1])

print('-=' * 30)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_coluna3}')
print(f'O maior valor da segunda linha é {maior_segunda}')