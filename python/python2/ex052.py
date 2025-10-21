numero = int(input('Digite um numero: '))
primo = 0
for c in range(1, numero+1):
    if numero % c == 0:
        primo += 1
if primo == 2:
     print('Esse numero é primo')
else:
     print('Esse numero nao é primo')
          