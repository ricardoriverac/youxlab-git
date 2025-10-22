#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for.

number = int(input('Digite um número para verificar a tabuada dele: '))
print(f'Tabuada do número {number}: ')
for conta in range(0, 11):
    result = number * conta
    print(f'{number} x {conta} = {result}')
