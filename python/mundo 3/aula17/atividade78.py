menor = 100000
maior = 0
minha_tupla = () 
for c in range (0,5):
    valor = int(input("digite um numero: "))
    minha_tupla += (valor,)    
    if valor > maior:
        maior = valor
    if valor < menor:
       menor = valor
posicao = minha_tupla.index(maior)
posicao_menor = minha_tupla.index(menor)
print(f"voce digiotu todos esses numeros {minha_tupla}")
print(f"o maior valor digitado foi {maior} na posicao {posicao}")
print (f"o menor valor digitado foi {menor} ea posiçao e {posicao_menor}")