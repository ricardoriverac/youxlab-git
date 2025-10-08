# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

valor = '' 
valores = []
pares = []
impares = []
while valor != 'sair':
    valor = str(input('Digite um valor [ou sair para encerrar]: '))

    if valor != 'sair':
        valor = int(valor)
        print(valor) 
        valores.append(valor)

        if valor % 2 == 0:
            pares.append(valor)
        
        else:
            impares.append(valor)

print('-'*60)
print(f'Os valores digitados são: {valores}')
print('-'*60)
print(f'Os valores pares saõ: {pares}')
print('-'*60)
print(f'Os valores impares são: {impares}')
print('-'*60)





