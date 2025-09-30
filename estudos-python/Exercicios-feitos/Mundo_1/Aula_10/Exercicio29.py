carSpeed = float(input('Enter your car speed - '))
if carSpeed <= 80:
    print ('You are free to go!')
else:
    value = ((carSpeed - 80)*7)
    print ('You got caught!')
    print (f'Now you have to pay ${value:.2f}')