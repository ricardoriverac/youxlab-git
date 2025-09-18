p=float(input('Qual o preço do produto? '))
fp=int(input("""Qual a forma de pagamento?
Digite 1 para A vista ou cheque
Digite 2 para A vista no cartao
Digite 3 para parcelar no cartao
Opcao escolhida: """))
if fp==1:
    print('Voce deverá pagar {}R$'.format(p-(p*0.10)))
elif fp==2:
    print('Voce deverá pagar {}R$'.format(p-(p*0.05)))
elif fp==3:
    np=int(input('Quantas vezes deseja parcelar?'))
    if np<=2:
        print('Voce pagará {}R$ e cada parcela ficará em {}R$'.format(p, p/np))
    elif np>=3:
        print('Voce pagará {}R$ em {} parcelas e o valor de cada parcela ficará em {}R$'.format(p+(p*0.20), np, p*1.20/np))