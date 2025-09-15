from datetime import date
yearOfBirth = int(input('Enter your year of birth: '))
actualYear = (date.today().year)
yourAge = actualYear - yearOfBirth
if 0<=yourAge<=9:
    print ('You are a MIRIM!')
elif 10<=yourAge<=14:
    print ('You are a INFANTIL!')
elif 15<=yourAge<=19:
    print ('You are a JUNIOR!')
elif 20<=yourAge<=21:
    print ('You are a SENIOR!')
elif 21<yourAge:
    print ('You are a MASTER!')