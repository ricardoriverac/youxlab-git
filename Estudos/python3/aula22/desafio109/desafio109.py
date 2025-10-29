import moeda

n=int(input('Digite o preço: R$ '))







print(f'A metade do preço de R${moeda.monetario (n)} é R${moeda.metade(n, False)}')
print(f'O dobro do preço R${moeda.monetario(n)} é R${moeda.dobro(n, True)}')
print(f'O preço R${moeda.monetario(n)} com aumento de 10% passa a valer R${moeda.aumento(n, True)}')