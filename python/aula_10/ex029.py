velocidade = float(input('Qual é a velocidade atual do seu veiculo?'))
multa = (velocidade - 80)*7
if velocidade >= 80:
    print(f'Você foi multado no valor de {multa}')
else:
    print('Tenha um bom dia! Dirija com segurança!')