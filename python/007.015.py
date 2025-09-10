carro= float(input('Por quantos dias você usou? '))
km_rodados= float(input('Quantos km você percorreu? '))
valor_carro= carro*60
valor_km= km_rodados*0.60
total= valor_km+valor_carro
print(f'Vocẽ ira pagar\nR${valor_carro} dos dias\nR${valor_km} do km rodado\nSomando o total de R${total}')