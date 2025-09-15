quilometos = int(input('Digite a quantos Km/h você estavá: '))
if quilometos > 80:
    print(f'Você foi multado em R${quilometos * 7} por ultrapassar o limite de 80 Km/h.')
else:
    print('Você estavá dentro do limite de velocidade!')