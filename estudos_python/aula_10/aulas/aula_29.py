'''
Escreva um programa que leia a velocidade de um carro.
Sa ele ultrapassar 80Km/h, mostra uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por cada Km acima do limite.
'''

#Resposta

quantos_km = int(input('Digite quanto km/h o carro esta: '))
ta_maluco = ((quantos_km - 80)*7)

if quantos_km > 80:
    print('Você foi multado!!')
    print(f'Essa e o valor da multa: {ta_maluco}')
else :
    print('Você esta no limite permitido!!')