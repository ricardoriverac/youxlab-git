# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = (
    ('Batom', 21.50),
    ('Blush', 45.99),
    ('Delineador', 12.00),
    ('Gloss', 43.25),
    ('Pó', 25.50)
)
print("-" * 90)
print(f"{'lista':>15} | {'Preço (R$)':<10}")
print("-" * 90)
for produto, preco in lista:
    print(f'{produto:>15} | {preco:>10.2f}')
print("-" * 90)
