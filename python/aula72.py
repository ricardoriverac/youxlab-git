
num_extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte' )
num = int(input('digite um numero entre 0 e 20:'))
while num <= 0 or num >= 20:
    print('tente novamente. digite um numero ntre 0 e 20:')
    num = int(input('digite um numero entre 0 e 20: '))

print(num_extenso[num])