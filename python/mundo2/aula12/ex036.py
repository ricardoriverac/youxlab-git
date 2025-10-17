# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Digite o valor da casa que deseja comprar: R$'))
salar = float(input('Digite o seu salário: R$'))
anos = float(input('Digite em quantos anos você irá pagar a casa: '))
mes_pagar = anos * 12
prestacao = valor / mes_pagar
limite = salar * 0.30
if prestacao <= limite:
    print('Empréstimo aprovado!')
    print(f'O valor a ser pago do empréstimo é de R${prestacao:.2f}')
else:
    print('O empréstimo foi negado.')