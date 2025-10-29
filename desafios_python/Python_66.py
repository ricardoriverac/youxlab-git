contador = 0 
soma = 0

while True:
    numero = int(input('Digite um valor (digite 999 para parar):'))
    
    if numero == 999:
        print('Você saiu do programa!')
        break

    contador += 1
    soma += numero
print('Você utilizou {} números e a soma desses valores foi {}'.format(contador,soma))

