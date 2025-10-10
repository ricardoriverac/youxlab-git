import time
nome=str(input('digite seu numero inteiro ')).strip()
time.sleep(1)
print('analizando seu nome...')
time.sleep(1)
print('Seu nome em maíusculo é {} '.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
