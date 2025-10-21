'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

'''
listaDnumeros = []
continuar = 'S'

while continuar == 'S':
    numero = int(input("Digite um número: "))
    if numero in listaDnumeros:
        numero = int(input("Esse número já foi adicionado. Adicione outro: "))
        listaDnumeros.append(numero)
    else:
        listaDnumeros.append(numero)
    print(listaDnumeros)
    continuar = str(input('Voce quer continuar [S/N]? ')).upper()     
print(sorted(listaDnumeros)) 
    


