'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a 
possibilidade da digitação de um número de tipo inválido. Aproveite e crie 
também uma função leiaFloat() com a mesma funcionalidade.
'''

#Resposta

#Número inteiro
def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
                            
        except KeyboardInterrupt:
                print('Valor invalido')
                continue
        except ValueError:
                print('Valor invalido!!') 
                continue
        except TypeError:
                print('Valor invalido!')
                continue

        else:
            print('Certo')
            b = valor
            return b

            
    
#Número quebrado
def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
                            
        except KeyboardInterrupt:
                print('Valor invalido')
                continue
        except ValueError:
                print('Valor invalido!!')
                continue
        except TypeError:
                print('Valor invalido!')
                continue
        else:
            print('Certo')
            b = valor
            return b


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número quebrado: ')