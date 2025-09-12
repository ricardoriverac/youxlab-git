firstSegment = float(input('Enter the size of the first segment'))
secondSegment = float(input('Enter the size of the second segment'))
thirdSegment = float(input('Enter the size of the third segment'))
if firstSegment + secondSegment > thirdSegment and firstSegment + thirdSegment > secondSegment and secondSegment + thirdSegment > firstSegment:
    print ('It is possible to make a triangle')
else:
    print ('It is not possible to make a triangle')