tupla = (input('Enter a word: ').strip().upper(),input('Enter a word: ').strip().upper(),input('Enter a word: ').strip().upper(),input('Enter a word: ').strip().upper(),input('Enter a word: ').strip().upper(),input('Enter a word: ').strip().upper())
for tup in tupla:
    print (tup)
    if 'A' in tup:
        ANumber = tup.count('A')
        print (f'There is {ANumber} A')
    else:
        print ('There is no A')
    if 'E' in tup:
        ENumber = tup.count('E')
        print (f'There is {ENumber} E')
    else:
        print ('There is no E')
    if 'I' in tup:
        INumber = tup.count('I')
        print (f'There is {INumber} I')
    else:
        print ('There is no I')
    if 'O' in tup:
        ONumber = tup.count('O')
        print (f'There is {ONumber} O')
    else:
        print ('There is no O')
    if 'U' in tup:
        UNumber = tup.count('U')
        print (f'There is {UNumber} U')
    else:
        print ('There is no U')