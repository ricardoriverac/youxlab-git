import random
count=0
numero1= int(input('Escolha um número: '))
numero2= int(input('Escolha outro número: '))
numero3= int(input('Digite mais um número: '))
numero4= int(input('Digite o último número: '))
tupla= numero1, numero2, numero3, numero4
for n in tupla:
    if n % 2 == 0:
        count+=1
print(f'Você digitou os valores {tupla}')
sorteioFrequencia= random.choice(tupla)
numeroFrequencia= tupla.index(sorteioFrequencia)
analise= tupla.count(numeroFrequencia)
if analise > 1:
    print(f'O valor {sorteioFrequencia} apareceu {analise} vezes')
elif analise == 1:
    print(f'O valor {numero1} não se repetiu')
posiçãoNumero= random.choice(tupla)
posição=tupla.index(posiçãoNumero)
print(f'O número {posiçãoNumero} apareceu na {posição}ª posição')
print(f'A quantidade de números pares inseridas foram {count}')