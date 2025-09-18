primeiro_termo= float(input('Digite o valor do primeiro termo: '))
razao = float(input("Digite o valor da razão: "))
print("\nOs 10 primeiros termos da PA são:")

for pa in range(10):
    termo_atual = primeiro_termo + pa * razao
    print(termo_atual)