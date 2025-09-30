#Diz se é ou não um palíndromo
phrase = str(input('Enter a phrase that you think it is a palindrome: ').strip().upper())
words = phrase.split()
together = ''.join(words)
invertedPhrase = ''
print (f"You choose the phrase '{phrase}'")
for letter in range(len(together) -1, -1, -1):
    invertedPhrase += together[letter]
if together == invertedPhrase:
    print (f'The phrase {phrase} is a palindrome!')
else:
    print (f'The phrase {phrase} is not a palindrome!')