numero1 = int(input("digite um numero: "))
numero2 = int(input("digite outro numero: "))
print("""ESCOLHE OQ VC DESEJA FAZER
[1] somar
[2] multiplicar
[3] qual eo maior
[4] novos numeros
[5] sair do programa""")
opçao = int(input("sua opçao: "))
while opçao != 5:
    if opçao == 1:
        soma = numero1 + numero2
        print(f"a soma dos dois numeros e {soma}")
    if opçao == 2:
        multiplicaçao = numero1 * numero2
        print(f"A multiplicaçao de {numero2} e {numero1} e {multiplicaçao}")
    if opçao == 3:
        if    numero1 > numero2:
            print(f"o maior e {numero1 }")
        else:
            print(f"o maior e {numero2}")  
    else:
        opçao == 4
        numero2 = int(input("digite um numero: "))
        numero1 = int(input("digite outro numero: "))




    print("""ESCOLHE OQ VC DESEJA FAZER
[1] somar
[2] multiplicar
[3] qual eo maior
[4] novos numeros
[5] sair do programa""")
    opçao = int(input("sua opçao: "))        


