wage = float (input ('Enter your wage - '))
if wage > 1250:
    wage = wage + wage/10
    print (f'Your wage with a 10% bonus is {wage}')
elif wage <= 1250:
    wage = wage + wage * 0.15
    print (f'Your wage with a 15% bonus is {wage}')