primeiroValor= int(input('Qual o primeiro valor da progressão aritmética escolhido?: '))
razão= int(input('Qual a razão da progressão aritmética escolhida?: '))
termo=primeiroValor
count=1
total=0
SUPERPA=10
while SUPERPA != 0:
    total= total+SUPERPA
    while count <= total:
        print(f'{termo}>', end='')
        termo= razão+termo
        count +=1
    print('Pausa')
    SUPERPA= int(input('Quantos novos termos você quer adicionar? '))
print(f'Progressão finalizada com {total} termos mostrados')