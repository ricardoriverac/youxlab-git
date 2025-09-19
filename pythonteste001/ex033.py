a=int(input('Primeiro valor: '))
b=int(input('Segundo valor: '))
c=int(input('Terceiro valor: '))
if a<b and a<c:
    menor=a
if b<c and b<a:
    menor=b
if c<a and c<b:
    menor=c
if a>b and a>c:
    maior=a
if b>c and b>a:
    maior=b
if c>a and c>b:
    maior=c
print('O menor número é {} e o maior é {}'.format(menor,maior))
