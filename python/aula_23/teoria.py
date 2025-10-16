'''
print('OI')
#print(x)v #NÃO FUNCIONA
#TEM UMA FALHA PQ A VARIAVEL X NÃO EXISTE
#EXCESSÃO: NameError'''


'''n = int(input("Nùmero:"))
print(f'Você digitou o número {n}')
#EXCESSÃO: ValueError não recebeu valor inteiro'''

try:
    a = int(input('numerador:'))
    b = int(input('denominador: '))
    r = a/b      

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')


'''Exception'''
#NameError
#ValueError
#ZeroDivisionError
#TypeError 
#IndexError
#KeyError
#EOFError
#KeyBoardInterrupt
#OSError
#MemoryError
#ConectionError
#RuntimeError