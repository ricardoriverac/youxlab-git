try:
    a = int(input('Numerador: '))
    b = int(input('Denomidador: '))
    r = a/b
except (ValueError, TypeError):
    print('Problema com os tipos de dados informados')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
else:
    print(f'O resultador é {r:.1f}')
finally:
    print('Volte sempre!')