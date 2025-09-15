from datetime import date
yearOfBirth = int(input('Enter your year of birth -'))
actualYear = (date.today().year)
if actualYear - yearOfBirth == 18:
    print ('You can enlist in the army!')
elif actualYear - yearOfBirth < 18:
    yearsLeft = (yearOfBirth - actualYear + 18)
    print (f'{yearsLeft} years left until enlistment!')
elif actualYear - yearOfBirth > 18:
    print ("You can't enlist anymore! Too Old!")