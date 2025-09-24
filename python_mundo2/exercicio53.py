frase = str(input('Digite uma frase: ')).strip().upper()
frsc = frase.split()
frac = ''.join(frsc)
contrario = ''
for n in range(len(frac) -1, -1, -1):
    contrario += frac[n]
print (frac, contrario )
if contrario == frac :
    print ('A frase digitada é um palídromo')
else:
    print('A frase não é um palídromo :(')