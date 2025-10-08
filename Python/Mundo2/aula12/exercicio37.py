numero = int(input('Digite um numero qualquer: '))
print('''É escolha o tipo da converção: ' 
'[1] mudar para binario' 
'[2] mudar para octal' 
'[3] mudar para hexadecimal''')
opcao=int(input("Sua opção: "))

if opcao == 1:
    print (bin(numero))
elif opcao == 2:
    print (oct(numero))
elif opcao == 3:
    print(hex(numero))