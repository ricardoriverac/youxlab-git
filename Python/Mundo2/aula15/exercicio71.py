print ('=-' * 20)
print('BEM VINDO AO SEU CAIXA!')
print ('=-' * 20)
def calcular_cedulas(valor):
    cedulas = [50, 20, 10, 1]
    resultado = {}
    for cedulas in cedulas:
        if valor >= cedulas:
            quantidade = valor // cedulas
            resultado[cedulas] = quantidade
            valor -= quantidade * cedulas
    return resultado
valor_saque = int(input("Digite o valor do saque: "))
distribuicao_cedulas = calcular_cedulas(valor_saque)

print(f"\nPara o valor de R$ {valor_saque}:")
for cedula, quantidade in distribuicao_cedulas.items():
    print(f"{quantidade} cédula(s) de R$ {cedula}")