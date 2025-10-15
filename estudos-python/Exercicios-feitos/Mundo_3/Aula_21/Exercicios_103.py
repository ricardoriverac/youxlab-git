def ficha(name='someone', score='0'):
    print(f'Your name is {name} and you scored {score} goals')
name = str(input('Enter your name:\n->')).strip().capitalize()
score = str(input('Enter your score:\n->'))
ficha()