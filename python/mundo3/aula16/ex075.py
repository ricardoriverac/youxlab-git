#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares que aparece.


valor1= int(input('Digite um número: '))
valor2 = int(input('Digite um número: '))
valor3 = int(input('Digite um número: '))
valor4 = int(input('Digite um número: '))
num = (valor1, valor2, valor3, valor4)
tupla_valores = tuple(num)
print(f'Valores digitados: {num}')
contagem_9 = tupla_valores.count(9)
print(f'O valor 9 apareceu {contagem_9} vez.')
if 3 in num:
   posi_tres = num.index(3)
   print(f'O número 3 apareceu na posição {posi_tres}.')
else:
    print('Não apareceu o número 3 durante o programa.')
for n in num:
  if n % 2 == 0:
      print(f'O número par que apareceu durante o prorama foi "{n}".')
