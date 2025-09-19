conta = 0
valor = 0
for num in range(0, 500, 2):     
    if num % 3 == 0:                                    #num são os números de 0 até 50
        valor += 1
        conta += num
        print(' a soma de todos {} valores é {}'.format(valor, conta))