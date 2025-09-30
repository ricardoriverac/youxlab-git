from datetime import date
yearOfBirth = int(input('Enter your year of birth: '))
actualYear = (date.today().year)
yourAge = actualYear - yearOfBirth
if 0<=yourAge<=8:
    print ('You are a MIRIM!')
elif 9<=yourAge<=13:
    print ('You are a INFANTIL!')
elif 14<=yourAge<=18:
    print ('You are a JUNIOR!')
elif 19<=yourAge<=20:
    print ('You are a SENIOR!')
elif 21<yourAge:
    print ('You are a MASTER!')