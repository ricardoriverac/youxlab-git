# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por
# extenso, de zero até vinte. Seu programa deverá
# ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contador = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
escolha = int(input('Digite um número de 0 a 20:'))
if 0<= escolha <=20:
    print(f'Você escolheu o número {contador[escolha]}')
else:
    print('Esse número é inválido, digite de 0 a 20.')
