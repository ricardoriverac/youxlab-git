from utilidasCeV import moedas

n=int(input('Digite o preço: R$ '))







print(f'A metade do preço de R${moedas.monetario (n)} é R${moedas.metade(n, True)}')
print(f'O dobro do preço R${moedas.monetario(n)} é R${moedas.dobro(n, True)}')
print(f'O preço R${moedas.monetario(n)} com aumento de 10% passa a valer R${moedas.aumento(n, True)}')