preco_normal=float(input('Qual o valor do produto atual?: R$ '))
metodo_pagar=int(input('Qual o metodo de pagamento? \n'
"1: A vista\n"
"2: Cartão\n"
"3: Cartao até 2x\n"
"4: Cartao até 3x ou mais\n"
"Escolha uma opção: "))
a_vista=preco_normal*0.10
cartao=preco_normal*0.05
cartao2x=preco_normal
cartao3x=preco_normal*1.2

if metodo_pagar==1:
    desconto=preco_normal*0.10
    print(f"O preço do seu desconto de 10% será: {preco_normal-desconto:.2f}")
elif metodo_pagar==2:
    desconto=preco_normal*0.05
    print(f"O valor a pagar no cartao com o desconto será: {preco_normal-desconto:.2f}")
elif metodo_pagar==3:
    print(f"Com 2x no cartão sai por: {preco_normal:.2f}")
elif metodo_pagar==4:
    print(f"Com 3x ou mais no cartão sera: {cartao3x:.2f}")