sum = 0
count = 0
while True:
    number = int(input('Digite um número: '))
    if number == 999:
        break
    count += 1
    sum += number
print (f'The total sum is {sum}!')
print (f'and {count} diferents numbers were nedded!')