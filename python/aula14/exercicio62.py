primeiro = int(input('Digite o primeiro número: '))
razao = int(input('Digite a razão'))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:  
        print(f'{termo} ', end = '')    
        termo += razao  
        count += 1  
    print('pausa')
    mais = int(input('Quer adicionar mais algum número? '))
print(f'O total de termos é {total}')  
'''an = a1 + r
o código terá 2 laços de repetição
1 -> verá se o programa tem uma resposta agradável a condição de repetição
2 -> permitirá contar os 10 primeiros termos
depois, você irá trocar a condição inicial do segundo while, que originalmente era 10, para o objeto total'''
