valorCasa = float(input('Digite o valor da casa que deseja comprar: '))
salario = float(input('Digite quanto você recebe por mês: '))
anos = float(input('Digite em quantos anos você vai pagar a casa: '))
prestacao = ((valorCasa / anos) / 12)
if prestacao < (0.30 * salario):
    print(f'PARABÉNS!! Você consiguirá financiar a casa! Com a mensalidade de {prestacao}')
else:
    print('EMPRESTIMO NEGADO! Infelizmente você não conseguirá financiar está casa!')