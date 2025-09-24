for c in range(0, 6): # ESCREVE OI 6 VEZES 
    print('Oi')
print('FIM') 


for c in range(6, 0, -1):
    print(c) # para escrever os numeros de 6 a 0  decrescente
print('FIM')

for c in range(0, 7): # para escrever de 0 a 6, pois não conta o número 7
    print(c)
print('FIM')

for c in range(0, 7, 2): #de 0 a 6 de 2 em 2
    print(c)
print('FIM')

n= int(input('Digite um número:')) #le um numero e vai de 0 até esse número
for c in range(0, n+1 ):
    print(c)
print('FIM')

i = int(input('Inicio: ')) 
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0, 3): 
    n = int(input('DIgite um valor: '))
print('fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')