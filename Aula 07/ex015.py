custo_dias = float(input('Por quantos dias o carro foi utilizado? '))
km_rodados = float(input('Por quantos km vc percorreu?'))
valor_carro = custo_dias*60
valor_km = km_rodados*0.60
total= valor_km+valor_carro 
print(f'Você ira pagar R${valor_carro} dos dias e R${valor_km} do km rodado\nSomando pagara no total R${total}  ')
