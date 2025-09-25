p = 'j'
while p not in 'MmFf':
    p = str(input('Digite qual seu sexo [M/F]')).upper()
print ('seu sexo é [{}]' .format(p))