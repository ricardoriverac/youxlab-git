#leia os catetos da hipotenusa e calcule ela
catetooposto = float(input('Comprimento do cateto oposto: '))
cateto =  float (input('Comprimento do cateto adiacente: '))
soma = (catetooposto ** 2 + cateto ** 2) ** (1/2)
print ('A hipotenuza vai medir {:.2}'.format(soma))