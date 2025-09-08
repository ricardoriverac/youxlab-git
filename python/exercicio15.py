dias = int(input('Por quantos dias voce alugou o carro: '))
kmr = float(input('O carro rodou quantos km: '))
preçod = dias * 60 
preçokm = kmr * 0.15
preçor = preçod + preçokm
print ('O valor do aluguel é {}R$, {}R$ por km andado e {}R$ por dias alugados' .format (preçor, preçokm, preçod))