nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota:"))
media = (nota1 + nota2) / 2
if media >= 7:
    print("voce passou de ano")
elif 5 <= media <= 6.9:
    print("voce esta de recuperaçao")
else: 
        print("voce esta reprovado")    
