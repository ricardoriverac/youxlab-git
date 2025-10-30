#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = float(input('Digite o primeiro termo da P.A: '))
razao = float(input('Digite a razão da P.A: '))
termo_atual = primeiro_termo
contador = 1
print('Os dez primeiros termo da progressão é')
while contador <= 10:
    print(f'{termo_atual }')
    termo_atual += razao
    contador += 1
