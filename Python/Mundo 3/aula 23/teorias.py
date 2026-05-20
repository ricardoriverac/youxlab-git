print('-'*50)
print('TRATAMENTO DE ERROS E EXCEÇÕES'.center(50))
print('-'*50)

try: #tente isso
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#except Exception as erro: #Se não, acontece essa exceção e mostrar o que deu de errado.
#    print(f'Problema encontrado foi: {erro.__class__}')

except (ValueError, TypeError):
    print('Tivemos problemas com os tipos de dados que você colocou.')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')


else: #Se não der problema
    print(f'    O resultado é: {r:.2f}')

finally: #Vai acontecer independente se deu certo ou errado.
    print(' VOLTE SEMPRE! Muito obrigado!')

#ValueEror = Erro no que o usuário digitou
#ZeroDivisionError = Erro de divisão por zero, não pode dividir um número por zero
#TypeError = Tipo do erro
#keyboardInterrupt = Não informar os dados que foram pedidos
