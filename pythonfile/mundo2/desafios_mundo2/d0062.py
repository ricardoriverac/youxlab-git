primeirovalor = int(input('Digite o primeiro valor: '))
razao = int(input('Qual a razão?: '))
termo = primeirovalor
count = 1
total = 0
progressao = 10
while progressao != 0:
    total = total+progressao
    while count <= total:
        print(f'{termo}', end='')
        termo = + termo
        count +=1
    print('\nPausa')
    progressao= int(input('Quais termos quer adicionar? '))
print(f'Progressão finalizada e o total de termos foi {total}')   