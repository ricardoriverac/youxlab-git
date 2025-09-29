numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo númeuro: '))
numero3 = int(input('Terceiro número: '))
if numero1 > numero2 and numero1 > numero3:
    print('O primeiro número é o maior!')
elif numero2 > numero3 and numero2 > numero1:
    print('O segundo número é o maior!')
elif numero3 > numero1 and numero3 > numero2:
    print('O terceiro número é o maior!')
else:
    print('Todos os número são iguais!')
