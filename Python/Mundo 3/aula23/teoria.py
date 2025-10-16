# Curso Python #23 - Tratamento de Erros e Exceções

# TEORIA
# Exceções
# valueERROR
# type
# indexError
# ModuleNoFoundERROR
# nameERROR 
# ZeroDivisionERROR
# keyERROR
# EOFError
# Keyboardinterrupt
# OSError
# MemoryError
# ConnectionError
# RuntimeError
 
# Exception -> exceção 
# try -> (operação) tente alguma coisa se não acontece uma exceção. 
# O Try pode ter vários except.
# except -> (falhou)
# -> except TypeError: and except ValueError: and except OSError: 
# else -> (deu certo)
# finally -> (certo/falha) acontece independentemente se deu certo ou errado.

# PRÁTICA 
# try: 
#     a=int(input('Numerador: '))
#     b=int(input('Denominador: '))
#     r=a/b
# except:
#     print('Tivemos um problema. :(')
# else:
#     print(f'O resultado é {r:.2f}')
# finally:
#     print('Volte sempre! ')

# try: 
#     a=int(input('Numerador: '))
#     b=int(input('Denominador: '))
#     r=a/b
# except Exception as erro:
#     print(f'O problema encontrado foi {erro.__class__} :(')
# else:
#     print(f'O resultado é {r:.2f}')
# finally:
#     print('Volte sempre! ')

try: 
    a=int(input('Numerador: '))
    b=int(input('Denominador: '))
    r=a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir o número por 0')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar os seus dados.')
except Exception as erro:
     print(f'O problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! ')

# Aleatório
"""
    Formata um valor numérico como moeda.
    :param preco: O valor a ser formatado.
    :param moeda: O símbolo da moeda.
    :return: O valor formatado como string.
    """