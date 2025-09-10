from datetime import datetime
dataDeNascimento= (input('Qual sua data de nascimento? ').replace("/", ""))
dataNova= int(dataDeNascimento[-4:])
anoAtual=datetime.now()
anoCorrente= anoAtual.year
idade= anoCorrente-dataNova
falta= 18-idade
prazoExpirado= 18-idade
if idade>18:
    print(f'Seu prazo para alistamento expirou! Se aliste o mais rápido possível! (Prazo expirado há {prazoExpirado} anos) ')
elif idade == 18:
    print('Você já pode se alistar!!')
else:
    print(f'Falta {falta} anos para você poder se alistar!')