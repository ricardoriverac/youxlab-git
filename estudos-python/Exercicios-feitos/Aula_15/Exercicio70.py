count = 0
sum = 0
cheapestPrice = 0
cheapestProduct = ""
expensiveProduct = 0
while True:
    product = str(input('Enter the product name'))
    price = float(input('Enter the product price'))
    sum += price
    count += 1
    if count == 1:
        cheapestPrice = price
        cheapestProduct = product
    if price < cheapestPrice:
        cheapestPrice = price
        cheapestProduct = product
    if price > 1000:
        expensiveProduct += 1
    doContinue = input('Do you want to continue?\n->').strip().upper()
    if doContinue != 'YES':
        break
print (f'You have to pay {sum:.2f} dollars!')
print (f'There is {expensiveProduct} products that cost more than 1000 dollars!')
print (f'And the cheapest product was {cheapestProduct}!')