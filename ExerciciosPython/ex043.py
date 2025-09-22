reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

# Verifica se as retas podem formar um triângulo
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print("Essas retas PODEM FORMAR um triângulo.")

    # Verifica o tipo de triângulo
    if reta1 == reta2 == reta3:
        print("É um triângulo EQUILÁTERO.")
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("É um triângulo ISÓCELES.")
    else:
        print("É um triângulo ESCALENO.")

else:
    print("Essas retas não PODEM FORMAR um triângulo.")