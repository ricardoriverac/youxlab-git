primeiroTermo = 0
segundoTermo = 1

for c in range(10):
    terceiroTermo = primeiroTermo + segundoTermo

    primeiroTermo = segundoTermo
    segundoTermo = terceiroTermo

    print(terceiroTermo, '_> ', end='')

# Explicação
# 0, 1, 1, 2, 3, 5, 8, 13, ....
# ele sempre vai começar com 0 e 1. 