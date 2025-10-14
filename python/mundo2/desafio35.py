print('--'*20)
print('analisador de triangulos')
print('--'*20)
r1 = float(input('primeiro segmento'))
r2 = float(input('primeiro segundo'))
r3 = float(input('primeiro terceiro'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem criar um triangulo')
else:
    print('os segmentos acima nao podem formar um triangulo')