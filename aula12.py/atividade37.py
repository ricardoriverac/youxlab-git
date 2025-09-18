numero = int(input(" digite um numero inteiro: ")) 
print(""" escolha uma das opçoes
[1]converter para binario
[2] converter para octal
[3]converter para hexadecimal""")
opçao = int(input("sua opçao: "))
if opçao == 1:
    print(f"{numero} convertido para binario e igual a {bin(numero)} [2:]")
elif opçao == 2:
    print(f"{numero} convertido ára Octal e igual a {oct(numero)} [2:] ") 
elif opçao == 3:
    print (f"{numero} convertido para Haxadecimal e igual a {hex(numero)} [2;]")     
else:
    print("opçao invalida,tente novamente")