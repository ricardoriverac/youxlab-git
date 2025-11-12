'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a 
possibilidade da digitação de um número de tipo inválido. Aproveite e crie 
também uma função leiaFloat() com a mesma funcionalidade.
'''

#Resposta

#Número inteiro
def leiaInt(msg):
    while b == False:
        try:
            valor = msg
            int(valor)
                            
        except KeyboardInterrupt:
                return print('Valor invalido')
        except ValueError:
                return print('Valor invalido!!') 
        except TypeError:
                return print('Valor invalido!')
        else:
            b = print('Certo')
            return
            
    
#Número quebrado
def leiaFloat(msg):
    while True:
        try:
            valor = msg
            float(valor)
                            
        except KeyboardInterrupt:
                return print('Valor invalido')
        except ValueError:
                return print('Valor invalido!!') 
        except TypeError:
                return print('Valor invalido!')
        else:
            return print('Certo')
            break


n1 = leiaInt(input('Digite um número inteiro: '))
# n2 = leiaFloat(input('Digite um número quebrado: '))