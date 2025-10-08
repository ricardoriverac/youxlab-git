def contador(início, fim, passo):
  print(f'Contando de {início} até {fim} com passo {passo}:')
  if passo > 0:
    for i in range(início, fim + 1, passo):
      print(i, end=' ')
  else:
    for i in range(início, fim - 1, passo):
      print(i, end=' ')
  print(' ') 
  
contador(1, 10, 1)
contador(10, 0, -2)
contador(5, 20, 3)