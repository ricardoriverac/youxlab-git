produtoNome = str(input('Qual o nome do produto?'))
preço= float((input('Qual o preço do produto?')))
juros = float((input('Qual o juros do produto? [%]')))
desconto =float((input('Qual o desconto do produto? [%]')))
jurosFinal= preço +(preço*juros/100)
descontoFinal= preço*desconto/100
print(f'O {produtoNome} à vista com desconto de {desconto}% custará {descontoFinal}\n O {produtoNome} parcelado com juros de {juros} custará {jurosFinal} ')