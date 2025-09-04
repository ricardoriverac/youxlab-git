dias=int(input('quantos dias alugados?: '))
km=float(input('quantos km rodados?: '))
diaria=dias * 60 + (km * 0.15)
print(f"O total a pagar é de {diaria}")