firstSide = float(input('Enter the first side size'))
secondSide = float(input('Enter the second side size'))
thirdSide = float(input('Enter the third side size'))
if firstSide == secondSide == thirdSide:
    print ('It is a equilateral triangle')
elif firstSide != secondSide != thirdSide:
    print ('It is a scalene triangle')
elif firstSide == secondSide != thirdSide or firstSide == thirdSide != secondSide or secondSide == thirdSide != firstSide:
    print ('It is a isosceles trinagle')