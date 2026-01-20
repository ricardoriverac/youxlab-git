#Adiciona valores dentro das listas
dados = []
lista = []

for c in range(0, 3):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))

    dados.append(nome)
    dados.append(idade)
    lista.append(dados[:])
    dados.clear()
    
for p, c in enumerate(lista):
    if c[1] >= 21:
        print(f'{c[0]} e maior de idade.')
    else:
        print(f'{c[0]} e menor de idade.')