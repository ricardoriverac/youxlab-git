soma = 0
for num2 in range (1, 7):                                     #numero de vezes que a pergunta vai se repetir
    num1 = int(input('Digite o {}º número: '. format(num2)))    #número digitado
    if num1 % 2 == 0:
        soma = soma + num1
print (soma)