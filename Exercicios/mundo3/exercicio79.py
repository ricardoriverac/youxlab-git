lista = []
continuar = 'S'


numero = int(input("Digite um número: "))
lista.append(numero)

while continuar != 'N':
    continuar = str(input('Quer continuar? [S/N]: ')).upper()




lista.sort()
print(f"Sua lista em ordem crescente é: {lista}")
    