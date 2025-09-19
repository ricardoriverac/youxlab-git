valorp = float(input('qual o valor do produto? '))                             #valor do produto
print ('digite [1] se for pagar em dinheiro/cheque')
print ('Digite [2] se for pagar à vista no cartão')
print ('Digite [3] se for pagar em até 2 vezes no cartão')
print ('Digite [4] se for pagar em mais de 2 parcelas ')
opcao = int(input('Qual o metodo de pagamento? '))
if opcao == 1:
    des = valorp * 10 / 100                                          #numero do desconto                        
    desc = valorp - des                                              #valor do produto com desconto aplicado
    print ('o valor do produto com o desconto de 10% é {}R$'.format(desc))
elif opcao == 2:
    des2 = valorp*5/100                                              #numero do desconto 
    desc2 = valorp - des2                                            #valor do produto com desconto aplicado 
    print ('O valor do produto com o desconto aplicado é de {}R$'.format(desc2))
elif opcao == 3 :
    print ('o produto não recebe nenhum desconto')
elif opcao == 4:
    alme = valorp * 20 / 100                                          #valor do juros
    valora = valorp + alme                                            #valor do produto com juros
    print ('O preço do produto ficou {}R$ com o juros'.format(valora))