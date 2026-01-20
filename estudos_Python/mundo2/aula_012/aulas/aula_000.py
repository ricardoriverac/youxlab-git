'''
Condições Aninhadas
'''

#elif

'''
O 'elif' pode ser utilizado para tem um terceira ou quarta opção
'''

'''
Ele pode ser utilizado depois do 'if' 
OBS:Ele pode ser utilizado sem o 'else' mas não sem o 'if'
'''

#Exemplo

numero = float(input('Digite o seu número favorito'))

if numero < 8 :

    print('E um bom numero')

elif numero > 8 or numero < 1615 :

  print('O número 8 e melhor')

elif numero == 0 :
 print('Número estranho')

else:
   print('PERFEITO')