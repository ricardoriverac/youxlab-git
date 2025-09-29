resto_da_divisao = 0
print("""
BANCO SICREDI"""       )
valor = int(input("digite o valor a ser sacado: R$ "))
print(f"{valor // 50} notas de 50R$")
resto_da_divisao = valor % 50
print(f"{resto_da_divisao // 20} notas de 20R$")
resto_da_divisao = resto_da_divisao % 20
print(f"{resto_da_divisao //10} notas de 10R$")
resto_da_divisao = resto_da_divisao % 10
print(f"{resto_da_divisao // 1} notas de 1R$")



    