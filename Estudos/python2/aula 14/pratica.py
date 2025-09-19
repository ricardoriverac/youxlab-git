#  Para fazermos: for c in range (1,10):
#                      print(c)
#                  print('FIM'!)
# Escrevemos:

c = 1
while c <10:
    print(c)
    c+=1
print('Fim')

# Para fazermos: for c in range (1, ?):
#                      print(c)
#                  print('FIM'!)
#  Escrevemos: 
n=1
while n != 0:
    n=int(input('Qual é o valor escolhido? '))
print('Fim')

# Para fazermos um sistema de continuação usamos:
r = 'S'
while r == 'S':
    n=int(input('Qual o valor escolhido? '))
    r=str(input('Quer continuar? [S/N]')).upper()
print('FIm')

# Para fazermos um sistema que conta quantos numeros pares ou impares foram digitados usamos:

n=1
par= impar = 0
while n != 0:
    n= int(input('Qual o valor escolhido?'))
    if n != 0:
        if n % 2 ==0:
            par+=1
        else:
            impar +=1
    print(f'Você digitou {par} números pares e {impar} números ímpares') 