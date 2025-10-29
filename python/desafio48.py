from time import sleep
for n in range (2, 51, 2):
    print('.',end ='')
    if n % 2 == 0:
     print(n,end='')
    sleep(0.5)
print ('acabou')

