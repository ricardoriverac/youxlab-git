lista = []
continuar = 'S'
while continuar == 'S':
    numero = int(input('Digite um valor: '))
    if numero in lista:
        print('ERRO. ESSE NÚMERO JÁ FOI DIGITADO')
    else:
        lista.append(numero)
        print(lista)
    continuar = str(input('Deseja continuar [S/N]:')).upper()
print(sorted(lista))       


    
