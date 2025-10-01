from random import randint
number = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print (number)
print (f'O menor número foi {sorted(number)[0]} e o maior foi {sorted(number)[4]}!')