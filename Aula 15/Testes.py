'''cont = 1 #while true --> vai rodar infinito 
while cont <=10:
    print(cont, '--> ', end='')
    cont +=1
print ('Acabou') '''



'''n= cont = 0
while cont < 5 :
    n = int(input('Digite um número: '))
    cont +=1'''


n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break      #para parar no 999
    s += n
print(f'A soma vale {s}')


nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos .')