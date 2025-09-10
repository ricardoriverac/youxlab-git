#Diz o seu primeiro nome e o último
fullName = input ('Enter your full name - ').strip()
fullName = fullName.split()
print ('O primeiro nome é {}'.format(fullName[0]))
print ('e o último é {}'.format(fullName[len(fullName)-1]))
