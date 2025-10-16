
try:
    print(x)

except Exception as erro:
    print(f'ERRO! o nome do erro é {erro.__class__}')
else:
    print('Deu certo')
finally:
    print('Volte sempre, muito obrigado! ')