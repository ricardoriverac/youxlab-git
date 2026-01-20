'''
Escrava um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''

#Resposta

digite_o_numero = int(input('Digite um número inteiro: '))

print('''
    Escolha qual opição deseja converter
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
      1 - Binário
      2 - Octal
      3 - Hexadecimal
''')

opicao = int(input('Escolha uma opição: '))

if opicao == 1 : 
   
   conversao_binario = f'{digite_o_numero:b}'
   print(conversao_binario)

elif opicao == 2 :
   
   conversao_octal = f'{digite_o_numero:o}'
   print(conversao_octal)

elif opicao == 3 :
   
   conversao_hexadecimal = f'{digite_o_numero:x}'
   print(conversao_hexadecimal)


else : 
   
   print('Essa opição e INEXISTENTE!!!')