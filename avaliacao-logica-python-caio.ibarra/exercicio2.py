numeros = []

for i in range(5):
    numeros.append(int(input(f'Digite o {i+1}° número:')))
print(f'O maior número digitado foi {max(numeros)}')
print(f'O menor número digitado foi {min(numeros)}')

soma = sum(numeros)
quantidade = len(numeros)
media = soma / quantidade
print(f'A média dos números digitados foi de {media}')

numerosORIginais = numeros[:]

numeros.sort()
print(f'Números que foram digitados em ordem crescente:{numeros}')

numeros.sort(reverse=True)
print(f'Números digitados em ordem decrescente:{numeros}')

numero = int(input('Digite um número para verificar se está na lista:'))

if numero in numerosORIginais:
    posicao = numerosORIginais.index(numero) + 1
    print(f'O número {numero} está na lista, na posição {posicao}')

else: 
    print(f'O número {numero} não está na lista')
