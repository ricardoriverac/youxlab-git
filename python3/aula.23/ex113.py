def leiaint(msg):
    while True:
        try:
          num = int(input(msg))
        except (ValueError,TypeError):
           print(f'O numero é INVALIDO por favor digite um numero inteiro valido')
           continue
        except KeyboardInterrupt:
           print('Entrada de dados interrompida pelo usuario')
           return 0
        else:
           return num
        
        

def leiafloat(msg):
    while True:
        try:
          num = float(input(msg))
        except (ValueError,TypeError):
           print(f'O numero é INVALIDO por favor digite um numero real')
           continue
        except KeyboardInterrupt:
           print('Entrada de dados interrompida pelo usuario')
           return 0
        else:
           return num
           

n1 = leiaint('Digite um numero: ')
n2 = leiafloat('Digite um numero: ')
print(f'O valor digitado foi {n1}, o valor real digitado foi {n2} ')
