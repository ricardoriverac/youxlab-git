
# numero = (valor1, valor2, valor3, valor4)
# print(f'Os valores digitados foram: {numero}')
# if numero.count(9) == 1:
#     print(f'O número 9 apareceu {numero.count(9)} vez')
# elif numero.count(9) == 0:
#     print('O número 9 não foi digitado')
# else:
#     print(f'O número 9 apareceu {numero.count(9)} vezes')
# if 3 in numero:
#     print(f'O primeiro número 3 foi digitado na {numero.index(3) + 1}ª posição')
# else:
#     print('Não tem nenhum número 3 nos valores digitados')
# print('Os valores pares digitados foram: ',end = '')
# for p in numero:
#     if p % 2 == 0:
#         print(p)


lista=list()
resposta='S'
while resposta != 'N':
    numero=int(input('Digite um valor: '))
    lista.append(numero)
    resposta=str(input('Quer continuar? S/N ')).upper()
print(f'Você digitou {len(lista)} elementos')
print(f'A ordem em decrescente é {lista.sort(reverse=True)}')
print(lista)
if 5 in lista:
    print(f'O valor 5 esta na lista.')
else:
    print(f'O valor  não esta na lista.')

