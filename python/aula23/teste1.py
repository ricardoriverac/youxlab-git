try:
    a = int(input('Numerador: '))
    b = int(input('Denomidador: '))
    r = a/b
except Exception as erro:
    print(f'Infelizmente tivemos um problema :(\nProblema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')