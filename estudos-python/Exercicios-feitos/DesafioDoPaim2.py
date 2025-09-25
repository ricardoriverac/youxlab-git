numero1 = float(input('Escolha um número: \n'))
numero2 = float(input('Escolha outro número: \n'))
menu=int(input('Escolha o que você quer fazer:\n[1]Somar:\n[2]Multiplicar: \n[3]Maior: \n[4]Novos númeuros: \n[5]Sair do Programa: \n'))
while menu != 5:
    if menu == 1:
        print ('Você escolheu a ação de somar\n')
        soma = (numero1 + numero2)
        print (f'A soma de {numero1} + {numero2} = {soma}!\n')
    elif menu == 2:
        print ('Você escolheu a ação de multiplicar\n')
        multiplicao = (numero1 * numero2)
        print (f'Você multiplicação entre {numero1} e {numero2} é igual a {multiplicao}!\n')
    elif menu == 3:
        print ('Você escolheu a ação de maior que\n')
        if numero1 > numero2:
            print (f'O número {numero1} é maior que o número {numero2}!\n')
        elif numero1 < numero2:
            print (f'O número {numero2} é maior que o número {numero1}!\n')
        else:
            print ('Eles são iguais!\n')
    elif menu == 4:
        print ('Você escolheu trocar de números!\n')
        numero1 = float(input('Escolha um número: \n'))
        numero2 = float(input('Escolha outro número: \n'))
    else:
        print ('Opção não reconhecida\n')
    menu=int(input('Escolha o que você quer fazer:\n[1]Somar:\n[2]Multiplicar: \n[3]Maior: \n[4]Novos númeuros: \n[5]Sair do Programa: \n'))
print ('Programa encerrado!\n')