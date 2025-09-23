from datetime import date
actualYear = (date.today().year)
totalMaior = 0
totalMenor = 0
for person in range(1,8):
    yearOfBirth = int(input(f'What year was the {person} person born?: '))
    age = actualYear - yearOfBirth
    if age >= 21:
        totalMaior += 1
        print (f'This person is {age} years old!\nThis person is of legal age!')
    else:
        totalMenor += 1
        print (f'This person is {age} years old!\nThis person is underage!')
print (f'We got a total of {totalMenor} person of legal age!')
print (f'We got a total of {totalMaior} minors')