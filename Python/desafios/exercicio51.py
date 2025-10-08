primeiro_termo = float(input('Digite o primeiro termo da P.A: '))
razao = float(input('Digite a razão da sua P.A: '))
print('-='*20)
print('10 TERMOS DA P.A : ')('0:17:8')
print('-='*20)
termo_atual = primeiro_termo
for i in range (10):
    print(termo_atual, end = " ")
    termo_atual += razao
    
print('ACABOU')