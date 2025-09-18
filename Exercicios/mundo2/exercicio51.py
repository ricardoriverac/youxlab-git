#primeiro_termo=int(input('Digite o primeiro termo de uma PA: '))
#razao=int(input('Digite a razão de uma PA: '))
#an=primeiro_termo
#
#for progressao in  range (0,11):
#    print

primeiro_termo= float(input("Digite o valor do primeiro termo: "))
razao = float(input("Digite o valor da razão: "))
print("\nos 10 primeiros termos da PA são:")
for pa in range(10):
    termo_atual = primeiro_termo + pa * razao
    print(termo_atual)