valores = []
listapar = []
listaimpar = []
for c in range(0,8):
    valores.append(int(input('Digite um valor: ')))
    print(valores)
for v in valores:
 if v % 2 == 0:
     listapar.append(v)
else:
    listaimpar.append(v)
print(f'Entre os valores digitados {sorted(listapar)} sao pares e {sorted(listaimpar)} sao impares')

