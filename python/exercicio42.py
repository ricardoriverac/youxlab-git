a = float(input("Digite o comprimento do primeiro segmento: "))
b = float(input("Digite o comprimento do segundo segmento: "))
c = float(input("Digite o comprimento do terceiro segmento: "))
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos PODEM FORMAR UM TRIÂNGULO!")
    if a == b and b == c:
        print("É um triângulo EQUILÁTERO.")
    elif a == b or b == c or a == c:
        print("É um triângulo ISÓSCELES.")
    else:
        print("É um triângulo ESCALENO.")
else:
    print("Os segmentos NÃO PODEM FORMAR UM TRIÂNGULO.")