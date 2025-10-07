contador=('zero','um','dois','tres','quatro','cinco','seis','sete', 'oito','nove','dez','onze',
'doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
valor=int(input('Escolha um valor de 0 a 20: '))
while True:
    if valor>=0 and valor<=20:
        break
    valor=int(input('Tente novamente: '))
print(f'O valor escolhido foi {contador[valor]}') 