# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

valores = []

valor = ''

while valor != 'sair':
    valor = str(input('Digite o valor[ ou sair para encerrar]: '))

    if valor != 'sair':
        valor = int(valor)
        if valor not in valores:
            valores.append(valor) 
        
print(f'Os valores digitados são: {sorted(valores)}') # sorted() - organiza so no momento, dentro dos {} // sort() - deixa o codigo em o



