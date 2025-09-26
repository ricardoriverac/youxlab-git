reta1 = float(input('Digite a sua primeira reta: '))
reta2 = float(input('Digite a sua segunda reta: '))
reta3 = float(input('Digite a sua terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print("Essas retas PODEM FORMAR um triângulo.")
else:
    print("Essas retas não PODEM FORMAR um triângulo.")
