#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.


matriz = []
for l in range(3):
    lista = []
    for coluna in range(3):
        num = int(input('Digite um número: '))
        lista.append(num)
    matriz.append(lista)
print('Matriz:')
for l in matriz:
    print(l)