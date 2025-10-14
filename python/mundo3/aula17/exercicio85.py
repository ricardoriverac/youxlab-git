listaUnica=[[],[]]

for i in range(1, 8):
    valor=int(input(f'Digite o {i}º valor: '))
    
    if valor % 2 == 0:
        listaUnica[0].append(valor)
    else:
        listaUnica[1].append(valor)

        
print(f'A lista de numeros pares é {sorted(listaUnica[0])}')
print(f'A lista de numeros impares é {sorted(listaUnica[1])}')

