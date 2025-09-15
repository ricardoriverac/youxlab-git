carro=int(input('Qual a velocidade do seu carro?: '))
multa=(80)

if carro>multa:
    print("Você foi multado! ")
    valor_multa=7.00
    subtrair= carro - multa
    valor_a_pagar=subtrair*valor_multa
    print(f" O valor da sua multa é: {valor_a_pagar}")
else:
    print("Nao foi multado!")
