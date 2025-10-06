'''
 Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
 No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
 '''

lista = []
for l in range(0, 5):
    valor = int(input('adicione um valor para que possamos ler: '))
    if l ==0:
        lista.append(valor)
    elif valor > lista[-1]:
        lista.append (valor)
    else:
        tantas = 0
        while tantas < len(lista):
            if valor <= lista[tantas]:
                lista.insert(tantas, valor)
                break 
            tantas += 1
print('=' * 50)
print('a lista em oredem ficou desta forma: {}'.format(lista))