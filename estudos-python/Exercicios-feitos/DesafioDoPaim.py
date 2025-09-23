phrase = str(input('Enter a phrase that you think it is a palindrome: ').strip().upper())
words = phrase.split()
together = ''.join(words)
invertedPhrase = together[::-1]
if together == invertedPhrase:
    print ('This phrase is a palindrome!')
else:
    print ('It is not a palindrome!')