Score1 = float(input('Enter the first test score: '))
Score2 = float(input('Now enter the second test score: '))
average = float((Score1 + Score2) / 2)
if average >= 7:
    print ('You got approved')
elif 5.0 <= average and average <= 6.9:
    print ('You need to do grade recovery')
elif average <= 4.9:
    print ('You failed')