'''
 Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário 
 digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados 
 e qual foi a soma entre elas (desconsiderando o flag).
'''

#Resposta

digite_numero = 0 
repeticao = True
contador = 0
soma = 0

while repeticao == True:
    contador += 1
    digite_numero = int(input('Digite qualque número[digite 999 para parar]: '))
    if digite_numero == 999:
        contador -= 1
        break
    
    soma += digite_numero

print(f'''A quantidade de números que foram digitados foi {contador}.
E a soma de todos os números e {soma}.''')
        