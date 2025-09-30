maior = 0
menor = 0
for person in range(1, 6):
    peso = float(input(f'Enter the {person}° weight: '))
    if person == 1:
        maior = person
        menor = person
    else:
        if peso > maior:
            maior = person
        if peso < menor:
            menor = person
print (f'The heaviest person is at {maior}° place!')
print (f'The lightest person is at {menor}° place!')