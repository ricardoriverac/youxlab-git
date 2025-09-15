print('-='*20)
print('Analisador de triangulos')
print('-='*20)
name1=float(input('Primeiro segmento: '))
name2=float(input('Segundo segmento: '))
name3=float(input('Terceiro segmento: '))
if name1<name2+name3 and name2<name1+name3 and name3<name1+name2:
    print('Os segmentos acima podem forma triangulo!')
else:
    print('Os segmentos acima NAO PODEM FORMA!')