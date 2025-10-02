lista = []
numero_par = []
numero_impar = []
while True:
    numero = int(input("digite um numero: "))
    resposta = str(input("quer continuar [s/n] ")).lower()
    lista.append(numero)
    #for numero in lista: 
    if numero  % 2 == 0:      
            numero_par.append(numero)
    else:
          numero_impar.append(numero)    
    if resposta == "n":
            break    
print(f"o total de numeros e {lista} os pares sao {numero_par} eos numeros impares sao {numero_impar} ")            