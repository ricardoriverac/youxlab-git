import random
numeroUm = random.randint(1, 10)
numeroDois = random.randint(1, 10)
numeroTres = random.randint(1, 10)
numeroQuatro = random.randint(1, 10)
numeroCinco = random.randint(1, 10)
numerosAleatorios = (numeroUm, numeroDois, numeroTres, numeroQuatro, numeroCinco)

print(f'Os números sorteados foram: {numerosAleatorios}')
print(f'o maior número é {max(numerosAleatorios)}')
print(f'O menor número é {min(numerosAleatorios)}')