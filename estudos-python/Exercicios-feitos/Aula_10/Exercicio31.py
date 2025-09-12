km = int (input('Kilometers traveled'))
if km <= 200:
    km = km*0.5
    print (f'{km:.2f}')
else:
    km = km*0.45
    print (f'{km:.2f}')