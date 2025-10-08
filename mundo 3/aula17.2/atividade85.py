valor_impar = list()
valor_par = list() 
lista_numeros = list()

for c in range (0,7):
    numero = int(input("digite um numero: "))
    lista_numeros.append(numero)
    if numero % 2 == 0:
        valor_par.append(numero)
    else:    
        valor_impar.append(numero)

print(f"""os numeros impares sao {sorted(valor_impar)}
os numeros pares sao {sorted(valor_par)}""")                 
        


