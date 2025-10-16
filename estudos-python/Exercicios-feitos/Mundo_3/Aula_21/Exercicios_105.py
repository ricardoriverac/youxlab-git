def score(* num, sit=False):
    """
    -> Make an dictionary and analysis some student score!
    It shows every added score
    The highest score
    The lowest score
    The average score
    And the situation
    """
    info = {}
    info['quantity']=len(num)
    info['lowest']=min(num)
    info['highest']=max(num)
    info['average']=sum(num)/len(num)
    if info['average'] >= 7:
        info['situation']=('You passed!')
    elif info['average'] >= 4:
        info['situation']=('You need to recover!')
    else:
        info['situation']=('You reproved')
    return info
numbers = []
while True:
    number = float(input('Enter the student score: '))
    if number == 999:
        break
    numbers.append(number)
help(score)
option = str(input('Do you want to know the situation?\nIf yes, enter [Y] or [y]')).strip().upper()
if option == 'Y':
    resultado=score(*numbers, sit=True)
else:
    resultado=score(*numbers, sit=False)
print(resultado)