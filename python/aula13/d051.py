primeiro_termo = int(input('Digite o primeiro termo: '))
quantidade = 10
razao = int(input('De quanto em quanto está indo: '))
for numero in range(quantidade):
    termo_atual = primeiro_termo + numero * razao
    print(termo_atual) 
    