#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.A multa vai custar R$7,00 por
# cada Km acima do limite.

car = int(input('Digite qual é a velocidade do seu carro: '))
if car  > 80 :
    print(f'Você foi multado, o seu veículo ultrapassou de 80km/h !')
multa = (car - 80) * 7
print(f'O valor a pagar dga multa é de R${multa}')