#a = int(input('Numerador: '))
#b = int(input('Denominador: '))
#r = a / b
#print(f'O resultado é {r}')


#try:
 #   a = int(input('Numerador: '))
  #  b = int(input('Denominador: '))
   # r = a / b
#except:
 #   print('Infelizmente tivemos um problema ')
#print(f'O resultado é {r}')





#try:
 #   a = int(input('Numerador: '))
  #  b = int(input('Denominador: '))
   # r = a / b
#except:
 #   print('Infelizmente tivemos um problema ')
#else:
 #   print(f'O resultado é {r:.1f}')




#try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#except:
 #   print('Infelizmente tivemos um problema ')
#else:
 #   print(f'O resultado é {r:.1f}')
#finally:
 #   print('Volte sempre! Muito obrigado!')


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueErro, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionErro:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupy:
    print('Ousuário preferiu não informar os dados!')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')    



