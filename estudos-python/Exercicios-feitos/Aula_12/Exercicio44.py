cellphonePrice = float(input('Enter the cellphone price '))
paymentMode = int(input('Enter the payment mode\n0-Money/Payment Check\n1-Credit Card\n '))
productInstallments = int(input('Enter how many installments do you want to pay? '))
if paymentMode == 0 and productInstallments == 1:
    cellphonePrice = cellphonePrice * 0.9 / productInstallments
    print (f'The amount to be paid is {cellphonePrice} dollars!')
elif paymentMode == 1 and productInstallments == 1:
    cellphonePrice = cellphonePrice * 0.95 / productInstallments
    print (f'The amount to be paid is {cellphonePrice} dollars!')
elif paymentMode == 1 and productInstallments == 2:
    cellphonePrice = cellphonePrice / productInstallments
    print (f'The amount to be paid is 2X{cellphonePrice} dollars')
elif paymentMode == 1 and productInstallments >= 3:
    cellphonePrice = cellphonePrice / productInstallments * 1.2
    print (f'The amount to be paid is {productInstallments}X{cellphonePrice} dollars')
else:
    print ('Something is wrong!!!')