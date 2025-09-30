lista = []
conta = media = quantidade = 0
pergunta = 's'
numero = int(input('Digite um número: '))
while pergunta in 'Ss':
    pergunta = str(input('Quer prosseguir? [Ss/Nn]'))
    numero1 = int(input('Digite um número: '))
    conta = conta + numero1
    quantidade = quantidade + 1
    lista += [numero]
    media = conta / quantidade
    print(f'Você digitou {quantidade} números e a média é {media}')
    print(f'Maior número digitado: ', max(lista))
    print(f'Menor número digitado: ', min(lista))