numeroEscolhido= int(input('Qual valor vocẽ deseja escolher?: [999 para encerrar]'))
numero= numeroEscolhido
soma=0
count=0
while numero != 999:
    count+=1
    soma=soma+numero
    numero=int(input('Qual valor você deseja escolher?: [999 para encerrar]'))
print(f'Você digitou {count} numeros e a soma entre eles foi {soma}')

