preco = float(input('Preço das contas: R$'))
print("""FORMAS DE PAGAMENTO
      [1]Dinheiro/Cheque
      [2]Cartão
      [3]2x no cartão
      [4]3x ou mais""")
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100 )
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcelas = total / 2
    print(f'Sua compra será parcelada de 2x de R${preco:.2f} no cartão')
elif opcao == 4:
    total = preco 
    quantidade = int(input('Quantas parcelas? '))
    parcelas = total / quantidade
    print(f'Sua compra será parcelada em {quantidade}x de R${parcelas} COM JUROS ')
print(f'Sua compra de R${preco:.3f} vai custar R${parcelas:.2f} no final')
