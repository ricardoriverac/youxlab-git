numberList = []
for count in range(0,5):
    number = int(input('Choose a number: '))
    if count == 0:
        numberList.append(number)
        print (f'The number {number} was added at the end!')
    else:
        for i in range(len(numberList)):
            if number < numberList[i]:
                numberList.insert(i,number)
                print (f'The number {number} was added at the {i}° position!')
                break
            elif numberList[i] == numberList[-1]:
                numberList.append(number)
                print (f'The number {number} was added at the end!')
                break
print (numberList)