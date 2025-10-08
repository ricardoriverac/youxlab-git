num = [2,5,9,1]
num[2]= 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(0, 2)
num.pop(0)
if 7 in num:
    num.remove(7)
else:
    print(f'Não encontrei o número 100')
print(num)
print(f'Esta lista tem {len(num)} elementos')
valores= list()
valores.append(1)
valores.append(2)
valores.append(3)
print(valores)
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} tem o número {v}')
    a= [2,3,4,7]
b=a
b[2]=8
print(f'A lista A tem os seguintes elementos: {a}')
print(f'A lista B tem os seguintes elementos: {b}')
#QUANDO IGUALAMOS UMA VARIAVEL A UMA LISTA E DEPOIS TRATAMOS A VARIAVEL IGUAL UMA LISTA, NAO MODIFICAMOS APENAS A VARIAVEL, MAS TAMBÉM A LISTA ORIGINAL, A NAO SER QUE USEMOS [:] QUE CRIA UMA COPIA DOS VALORES DA LISTA ORIGINAL