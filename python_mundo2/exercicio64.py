n = 0
d = 0
t = 0
while n!= 999 :
    num = int(input('Digite um número: '))
    n = num
    if n != 999:
        d = d + n
        t = t + 1
    else:
        pass
print ('foram digitados {} números e a soma deles é {}' .format(t, d))
