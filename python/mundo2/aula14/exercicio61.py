primeiro=int(input('Primeiro termo: '))
razao=int(input('Razão: '))
contador=1
while contador<=10:
    termoatual=primeiro+(contador-1)*razao
    print(f'o termo {contador} é {termoatual}')
    contador+=1
    