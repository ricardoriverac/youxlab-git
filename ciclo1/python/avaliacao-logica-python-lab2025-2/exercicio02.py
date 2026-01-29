valores = []

for numeros in range(5):
    valor = int(input('Digite um valor: '))
    valores.append(valor)

media = sum(valores) / len(valores)
print(valores)
print(f'O maior valor da lista é: {max(valores)}')
print(f'E o menor valor é: {min(valores)}')
print(f'A media dos valores é: {media}')

crescente = sorted(valores)
decrescente = sorted(valores, reverse=True)
print(f'A lista em ordem crescente é: {crescente}, e a lista em ordem decrescente é {decrescente}')

numero_buscar = int(input("Qual número deseja procurar?: "))

if numero_buscar in valores:
    posicao = valores.index(numero_buscar)
    print(f'O número buscado está na posição: {posicao}')
else:
    print("Este número não existe na lista!")