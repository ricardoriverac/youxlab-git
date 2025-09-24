num = int(input('Digite um número: '))
numero0 = 0
for rnum in range (1, num+1):
    if num % rnum == 0 :
        numero0 = numero0 + 1
    else:
        pass
if numero0 == 2 :
    print ('O número {} é um número primo, ebaaa' .format(num))
else :
    print('O número {} não é um número primo :(' .format(num))