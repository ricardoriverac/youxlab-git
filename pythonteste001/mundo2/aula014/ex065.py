resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
             maior = numero
        if numero < menor:
            menor = numero
    resposta = (str(input('continuar?[S/N]: '))).upper().strip()[0]
media = soma / quantidade
print(f'a média desses {quantidade} números é {media}')
print(f'o maior número é {maior} e o menor é {menor}')
