#O que e Exception
'''
Exception: representa qualquer erro genérico que possa acontecer.
'''
#Explicando -> except Exception as erro:
'''
Ela captura qualquer erro (exceção) que aconteça dentro do bloco try
e guarda esse erro na variável erro.

1 -> Então, se algo der errado no try, o Python vai:

2 -> Parar de executar o try

3 -> Pular para o except

Criar uma variável chamada erro com informações sobre o que aconteceu
'''

#Exemplo
try:
    n1 = int(input('Digite o 1° número: '))
    n2 = int(input('Digite o 2° número: '))

    # código que pode gerar um erro
    resultado = n1 / n2
except Exception as erro:
    # o que fazer se der erro
    print("Ocorreu um erro!")

#except com outros tipos de erro

try:
    n1 = int(input('Digite o 1° número: '))
    n2 = int(input('Digite o 2° número: '))
    resultado = n1 / n2

except ZeroDivisionError:
    print("Não foi possivel dividir por 0!!")

except ValueError:
    print('Deu erro de valor!!!')