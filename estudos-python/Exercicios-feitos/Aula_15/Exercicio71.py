fiftyDollars = 0
twentyDollars = 0
tenDollars = 0
oneDollar = 0
while True:
    withdraw = int(input('How much do you want to withdraw?:'))
    value = withdraw
    if value / 50:
        fiftyDollars = value // 50
        value = value - (fiftyDollars * 50)
    if value / 20:
        twentyDollars = value // 20
        value = value - (twentyDollars * 20)
    if value / 10:
        tenDollars = value // 10
        value = value - (tenDollars * 10)
    if value / 1:
        oneDollar = value // 1
        value = value - (oneDollar * 1)
    break
print (f'You choose to withdraw {withdraw} dollars!')
print (f'You will receive:')
print (f'{fiftyDollars} 50 dollars bill')
print (f'{twentyDollars} 20 dollars bill')
print (f'{tenDollars} 10 dollars bill')
print (f'{oneDollar} 1 dollars bill')