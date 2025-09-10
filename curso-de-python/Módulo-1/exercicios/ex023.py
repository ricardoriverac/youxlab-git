numero = int(input('Informe o número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))

'''numero = int(input('Informe o número: '))
numero2 = str(numero)
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(numero2[3]))
print('Dezena: {}'.format(numero2[2]))
print('Centena: {}'.format(numero2[1]))
print('Milhar: {}'.format(numero2[0]))'''

'''Vídeo de exercício: https://youtu.be/wD2aerLMBWA?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6'''