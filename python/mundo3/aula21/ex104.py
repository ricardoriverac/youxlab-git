#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')

def leiaInt(num=0):
  num = input('Digite um número: ')
  if num.isnumeric():
    return int(num)
  else:
      print('ERRO, Digite um valor númerico válido: ')
      return num
numero = leiaInt()
print(f'O valor digitado foi: {numero}')




