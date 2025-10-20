import moeda #importar o modulo moeda pra pasta exercicio107

p = int(input('digite o preço: R$'))
print(f'aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13)}')
print(f'o dobro de R${p} e R${moeda.dobro(p)}')
print(f'a metade de R${p} e R${moeda.metade(p)}')