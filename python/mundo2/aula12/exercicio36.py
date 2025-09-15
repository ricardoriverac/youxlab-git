casa=float(input('Valor da casa: R$'))
salario=float(input('Salario do comprador: R$'))
anos=int(input('Quantos anos de financeamento? '))
prestação=casa/(anos*12)
minimo=salario*30/100
print(f'Para pagar uma casa de {casa} em {anos} anos')
print(f'a prestação sera de R${prestação}')
if prestação<=minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
