#Teoria da aula 15.
#Interrompendo repetições  while

numero = 0
while True:
    numero = int(input('Advinhe em qual número estou pensando: '))
    if numero == 15:
        break
print('Você acertou, FIM!')