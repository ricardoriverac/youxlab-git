ns = (int(input('Digite um número: ')), 
      int(input('Digite um número: ')),
      int(input('Digite um número: ')),
      int(input('Digite um número: ')))
print (f'Os números pares são os: ')
for n in ns:
    if n % 2 == 0:
        print (n)

print (f'Os números digitados foram {ns}, e o número três foi digitado na posição {ns.index(3)}')