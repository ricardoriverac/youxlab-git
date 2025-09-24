#break:vai interromper a reepetiçao while
#while True: vai fazer uma repetiçao infinita
n = soma =0 
while True:
    n = int(input('Digite um numero '))
    if n == 999:
        break
    soma += n 
print('A soma vale {soma}')