import random
megasena = []
numberGroups = []
tries = int(input('How many guesses would you like?: '))
while True:
    for p in range(tries):
        for c in range (6):
            numberGroups.append(int(random.randint(1,60)))
        megasena.append(numberGroups[:])
        numberGroups.clear()
    break
print (megasena)