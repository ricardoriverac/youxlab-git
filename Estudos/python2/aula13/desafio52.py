count=0
countDivisao=0
total=0
numeroSelecionado= int(input('Qual número você quer verificar? '))
for c in range (1, numeroSelecionado+1):
    print(c)
    if numeroSelecionado % c == 0:
        total= total+1
if total == 2:
    print (f'O número {numeroSelecionado} foi dividido {total} vezes, e por isso ele é PRIMO!')
else:
    print(f'O número {numeroSelecionado} foi dividido {total} vezes, e por isso ele NÃO É PRIMO! ')