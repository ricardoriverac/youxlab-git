primeiroTermo = float(input("Digite o primeiro termo da PA: "))
razao = float(input("Digite a razão da PA: "))
print("Os 10 primeiros termos da PA são:")
contador = 0
termoAtual = primeiroTermo
while contador < 10:
    print(termoAtual)
    termoAtual = primeiroTermo + razao
    contador = contador + 1