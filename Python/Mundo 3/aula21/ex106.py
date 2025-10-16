# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM',
# o programa se encerrará. Importante: use cores.

def ajuda(com):
    help(com)

comando=''
while True:
    comando= str(input('Função ou Bblioteca > '))
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)









