valores = []
valores = [int(input('digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')),
           int(input('Digite um valor: ')), int(input('Digite um valor: '))]
maior = max(valores)
manor = min(valores)
for v, c in enumerate(valores):
    print(f'Na posição {v} encontrei o valor {c}')
print (f'''O maior valor foi {maior} na {valores.index(max(valores)) + 1} posição, e o menor valor foi {manor} na posição {valores.index(min(valores)) + 1}''')