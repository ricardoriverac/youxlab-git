#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

continuar = 'S'
number_unicos = []
while continuar == 'S':
    valor = int(input('Digite um valor: '))
    if valor not in number_unicos:
        number_unicos.append(valor)
        print('Valor adicionado.')
    else:
        print('Já existe esse valor dentro da lista.')
    continuar = input('Voê deseja continuar:[S/N]').upper()
number_unicos.sort()
print(f'Valores únicos em ordem crescente: {number_unicos}')



