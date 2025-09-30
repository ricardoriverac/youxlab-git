numero = int(input('Digite um número: '))
fatorial = numero
resposta = numero
while fatorial != 1:
    resposta = resposta*fatorial
    print(f'O fatorial de {numero} é {resposta}')