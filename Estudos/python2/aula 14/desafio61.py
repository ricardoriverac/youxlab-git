print('Gerador de Progressão Aritmética')
print('-=' * 10)
primeiroTermo= int(input('Qual o primeiro termo da PA?: '))
razão=int(input('Qual a razão da PA?: ')) 
count=1
termo= primeiroTermo
while count <=10:
    print(f'{termo}>', end= '')
    termo= razão+termo
    count +=1
print('FIM')