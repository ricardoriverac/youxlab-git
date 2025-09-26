# Curso Python #15 - Interrompendo repetições while
# while true: >>>>>>>>>>>>>>>>>>>>>>>>> enquanto verdadeiro
#   if        >>>>>>>>>>>>>>>>>>>>>>>>> se 
# break       >>>>>>>>>>>>>>>>>>>>>>>>> interrompa

# PRÁTICA
# EX.:1  
# cont = 1
# while cont <= 10:
#   print(cont, '...', end='')
#   cont += 1
# print('Acabou')
# EX.:2
# cont = 1
# while True <= 10: # o comando 'True' é infinito
#   print(cont, '-> ', end='')
#   cont += 1
# print('Acabou')
# EX.:3
# numero = soma = 0
# while numero != 999:
#     numero = int(input('Digite um número: '))
#     soma += numero
# soma -= 999 
# print(f'A soma vale {soma}.')
# EX.:4
# numero = soma = 0
# while True:
#     numero = int(input('Digite um número: '))
#     if numero == 999:
#         break # interrompa
#     soma += numero 
# print(f'A soma vale {soma}.')
# EX.:5
nome = 'Júlia'
idade = 16
salario = 300.00
print(f'O {nome:-^20} tem {idade} anos  e ganha R${salario:.2f}')
