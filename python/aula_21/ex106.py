'''
Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
'''

def assunto(title, n):
    from time import sleep
    if n == 1:
        texto = title
        print('\033[30;42m', end='')
    elif n == 2:
        texto = f'Acessando o manual do comando "{title}"'
        print('\033[30;44m', end='')
    elif n == 3:
        texto = 'ATÉ LOGO!'
        print('\033[30;41m', end='')
    carac = len(texto) + 8
    print('~' * carac)
    print(f'    {texto}')
    print('~' * carac)
    if n == 2:
        sleep(1)
        print('\033[36;40m', end='')
        help(title)


while True:
    inicio = 'SISTEMA DE AJUDA PyHELP'
    assunto(inicio, 1)
    funbibl = str(input('\033[mFunção ou Biblioteca > ')).lower()
    if funbibl == 'fim':
        assunto(funbibl, 3)
        break
    assunto(funbibl, 2)