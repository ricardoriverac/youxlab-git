import moeda

n=int(input('Digite o preço: R$ '))







print(f'A metade do preço de R${moeda.monetario (n)} é R${moeda.monetario(round(moeda.metade(n)))}')
print(f'O dobro do preço R${moeda.monetario(n)} é R${moeda.monetario(round(moeda.dobro(n)))}')
print(f'O preço R${moeda.monetario(n)} com aumento de 10% passa a valer R${(moeda.monetario(round(moeda.aumento(n))))}')