casa1 = float(input('Valor da casas: R$'))
salario = float(input('Salário do comprador: R$'))
tempoAnos = int(input('Quantos anos de financiamento?:'))
prestacao = casa1 / (tempoAnos * 12)
print('Para pagar uma casa de R${:.2f} em {:.2f} anos '.format(casa1, tempoAnos,),end='')

print(', a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= (salario / 0.3):
    print("Emprestimo aceito com parcelas no valor de {:.2f}" .format(prestacao))
    
else: 
    print('Seu emprestimo foi negado')

