numero=int(input('Digite um numero: '))
print('''Escolha uma das bases para mudar:
[1] mudar para BINARIO
[2] mudar para OCTAL
[3] mudar para HEXADECIMAL''')
opçao=int(input("Sua opção: "))
 
if opçao==1:
    print(bin(numero))
elif opçao==2:
    print(oct(numero))
elif opçao==3:
    print(hex(numero))