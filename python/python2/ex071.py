valor = int(input('Qual valor voce quer sacar? '))
cedula = 50
nota50 = 0
nota20 = 0
nota10 = 0 
nota1 = 0
while True:
    if valor >=50:
        valor -= 50
        nota50 += 1
        
    else:
        if valor >= 20:
            valor -= 20
            nota20 += 1
            
        elif valor >= 10:
            valor -= 10
            nota10 += 1
            
        elif valor >= 1:
            valor -= 1
            nota1 += 1
            
        elif valor == 0:
            break

print(f"Total de {nota50} cédulas de R$50,00")
print(f"Total de {nota20} cédulas de R$20,00")
print(f"Total de {nota10} cédulas de R$10,00")
print(f"Total de {nota1} cédulas de R$1,00")      