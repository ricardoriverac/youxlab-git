# Faça um programa que deve ler um número inteiro pelo teclado (entre 0 e 20) e mostrar esse número por extenso. 
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
usuario = int(input('Digite um número de 0 a 20: '))
while usuario < 0 or usuario > 20:
    usuario = int(input('Número inválido. Digite novamente um número de 0 a 20: '))
print(numeros[usuario])