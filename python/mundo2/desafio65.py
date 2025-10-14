escolha='S'
media=count=soma=maior=menor=0
while escolha in'sS':
    x = int(input('Digite um valor: '))
    soma += x
    count += 1
    if count==1:
        maior = menor = x
    else:
        if x>maior:
            maior=x
        elif x<menor:
            menor=x
    escolha = str(input('Você quer continuar? [S] ou [N]: ')).strip().upper()[0]
    while escolha not in "SsNn":
        print('Escolha errada, digite S ou N')
        escolha = str(input('Você quer continuar? [S] ou [N]: ')).strip().upper()[0]
    media = soma / count
print('Você digitou {} valores, média da soma entre eles foi {}.'.format(count,media))
if maior > menor:
    print('O maior número foi {} e o menor foi {}'.format(maior, menor))
elif maior==menor:
    print('Os numéros tem o mesmo vaor, são iguais!')
print('FIM')
