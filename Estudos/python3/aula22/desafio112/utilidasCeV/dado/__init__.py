from utilidasCeV import moedas
def leiaDinheiro(p):
    if p.isdigit():
        p=int(p)
        print(f"""RESUMO DO VALOR
                   Preço analisado {p}
                   Dobro do preço:  {moedas.dobro(p, True)}
                   Metade do preço: {moedas.metade(p, True)}
                   35% de aumento:  {moedas.aumento(p, True)}
                   22% de redução:  {moedas.reducao(p, True)}""")
    else:
        p=p.strip()
        print(f'ERRO "{p}" não é um valor válido ')