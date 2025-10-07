
numerosExtenso= 'Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
while True:
    Usuario= int(input('Digite um numero de 0 a 20: '))
    if Usuario > 20 or Usuario<0:
        print('Tente novamente! ')
    print(f'Você digitou o número  {numerosExtenso[Usuario]}')
    continuação =str(input('Você quer continuar? [S/N]').upper())
    if continuação not in 'S':
        break
print('Programa encerrado!')
                
          