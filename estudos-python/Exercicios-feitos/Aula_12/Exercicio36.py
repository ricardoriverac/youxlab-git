housePrice =  float (input ('Enter the house price'))
yourWage = float (input ('Enter your wage'))
yearsToPay = int (input ('How many years do you want to pay?'))
monthlyInstallments = housePrice/ (yearsToPay * 12)
if monthlyInstallments > yourWage*0.3:
    print ('Your loan was denied! You cannot buy your house!')
else:
    print ('Your loan was accepted! You can buy your own house!')