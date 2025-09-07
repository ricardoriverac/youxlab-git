km = float(input('Qual foi a quantidade de km peercorridos pelo carro?'))
dias = int(input('Por quantos dias o carro foi alugado?'))
tkm = km * 0.15
total= dias * 60
aluguel = tkm + total 
print('O valor total a pagar é {}' .format(aluguel))