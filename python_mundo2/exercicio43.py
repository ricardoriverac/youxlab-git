import time
altura = float(input("Qual é a sua altura?"))
peso = float(input("Quantos kg você tem?"))
IMC = peso / (altura * 2)
if IMC < 18.5:
    print("Seu índice de massa ficou em {:.1f}, você está abaixo do peso!" .format(IMC))
elif IMC < 25:
    print("Seu IMC ficou em {:.1f}, você está no peso ideal!" .format(IMC))
elif IMC <= 30:
    print("Seu IMC ficou em {:.1f}, você está sobrepeso!" .format(IMC))
elif IMC <= 40:
    print("Seu IMC ficou em {:.1f}, você está em obesidade,tem que cuidar mais da saúde !" .format(IMC))
else:
    print("Seu IMC ficou em {:.1f}, você está em obesidade morbida, tem que cuidar rigorosamente da sua saúde!" .format(IMC))