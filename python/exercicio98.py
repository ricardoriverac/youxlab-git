def contador(início, fim, passo):# Função personalizada para contar de acordo com os parâmetros
  print(f'Contando de {início} até {fim} com passo {passo}:')
  if passo > 0:# Corrige passo 0 ou negativo
    for i in range(início, fim + 1, passo): # Lógica para contar crescente
      print(i, end=' ')
  else:
    for i in range(início, fim - 1, passo):   # Lógica para contar decrescente
      print(i, end=' ')
  print(' ') 
contador(1, 10, 1)# Conta de 1 até 10 de 1 em 1
contador(10, 0, -2)# Conta de 10 até 0 de 2 em 2 para trás
contador(5, 20, 3) # Conta de 5 até 20 de 3 em 3