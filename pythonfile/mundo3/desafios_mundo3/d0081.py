lista = []
contador = 0

while True:
    numeros = int(input('Digite numeros: '))

    if numeros not in lista:
        lista.append(numeros)
        resposta = input('Quer continuar [S/N]? ').upper()
        contador == numeros
        contador += 1
        
        if resposta == 'N':
            break

lista.sort(reverse=True)
print(f'Foi digitado {contador} numeros')
print(f'A lista em ordem decrescente: {lista}')
print(f'O numero 5 esta {(lista.index(5))} posição')