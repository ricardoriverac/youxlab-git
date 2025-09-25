primeirovalor = int(input('Digite o primeiro valor: '))
razao = int(input('Qual a razão?: '))
termo = primeirovalor
contador = 1
total = 0
progressao = 10
while progressao != 0:
    total = total+progressao
    while contador <= total:
        print(f'{termo}', end=' ')
        termo += razao
        contador +=1
    print('Pausa')
    progressao= int(input('Quais termos quer adicionar? '))
print(f'Progressão finalizada e o total de termos foi {total}')   