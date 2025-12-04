def leiaDinheiro(mone='Digite um valor monetário: '):
  while True:
      try:
          entrada = input('Digite um valor monetário:R$')
          valor = float(entrada)
          return valor
      except ValueError:
          print('\033[1;31mERRO, digite o valor monetário corretamente\033[0m')
valor_recebido = leiaDinheiro()
print(f'Valor monetário recebido:R${valor_recebido}')

