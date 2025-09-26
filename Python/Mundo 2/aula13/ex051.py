primeiroTermo = float(input("Digite o primeiro termo da PA: "))
razao = float(input("Digite a razão da PA: "))
print("Os 10 primeiros termos da PA são:")
for c in range(10):
    termoAtual = primeiroTermo + c * razao
    print(termoAtual)