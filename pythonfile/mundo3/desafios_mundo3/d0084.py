pessoas = list()
dados = list()
cadastros = 0
maior = 0
menor = 0

while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    
    pessoas.append(nome)
    dados.append(peso)
    cadastros += 1

    if cadastros == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    resposta = input('Quer continuar? [S/N] ').upper()
    if resposta == 'N':
        break

print(f'\nO total de pessoas cadastradas foi {cadastros}')
print(f'A pessoa mais pesada tem {maior}Kg e a mais leve tem {menor}Kg')










