#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar
# o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Importante: use cores.


nome = input('\033[1;31mDigite seu nome: ')
print(f'\033[1;31mSeja Bem-Vindo {nome}.')
help(print)
