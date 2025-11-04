# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.
guarda_numero = []
resposta = 's'
while resposta != 'n':
    numero = int(input('Digite um número inteiro: '))
    guarda_numero.append(numero)
    resposta = str(input('Deseja continuar [S/N]')).lower()
media = sum (guarda_numero) / len(guarda_numero)
maior = max(guarda_numero)
menor= min(guarda_numero)
print(f'O maior número é {maior} e o menor é {menor} e a média entre eles é {media:.2f}')