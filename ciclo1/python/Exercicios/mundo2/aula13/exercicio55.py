peso_maior=0
peso_menor=1000

for peso in range (5):
    peso_da_pessoa=float(input(f"Digite o peso da {peso+1}ª pessoa: "))
    if peso_da_pessoa>peso_maior:
        peso_maior=peso_da_pessoa
    
    if peso_da_pessoa<peso_menor:
        peso_menor=peso_da_pessoa
print(f"\nO maior peso foi {peso_maior}")
print(f"E o menor foi {peso_menor}")
