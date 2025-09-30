option = input('Iniacialize program?\n[N]No [Y]Yes').strip().upper()
ofLegalAge = 0
mans = 0
womansUnder20 = 0
while True:
    while option == 'Y':
        age = int(input('What is your age?'))
        sex = int(input('What is your gender?\n[1]Male [2]Female'))
        if age > 18:
            ofLegalAge += 1
        if sex == 1:
            mans += 1
        if sex == 2 and age < 20:
            womansUnder20 += 1
        option = input('Do you want to continue the program?\n[N]No [Y]Yes').strip().upper()
    break
print (f'There is {ofLegalAge} peoples of legal age!')
print (f'There is {mans} mans!')
print (f'And there are {womansUnder20} womans under 20 years!')